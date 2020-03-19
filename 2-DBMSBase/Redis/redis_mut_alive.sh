#!/bin/bash
#wangxuexian

# 目标: 检查redis实例存活

# /usr/bin/redis-cli -p $port ping 检测存活(5次)
# 异常时判断故障类型: shutdown 或 连接满(ERR max number of clients reached)
# 告警信息:
#   shutdown -- port:$port;status:down
#   连接满   -- port:$port;status:ERR max number of clients reached
# 非Sentinel服务时, 检查同步信息 master_link_status, master_host, master_port
#   /usr/bin/redis-cli -p $port info replication
# 当 master_link_status为down时异常(5次)
# 告警信息:
#   slave[...] -> master[..];status:master_link_status  down

[[ $(ps -ef|grep -c $0) -gt 4 ]] && exit 0
[[ ! -d /etc/snmp/yyms_agent_redis_scripts ]] && exit 0

export PATH=/data1/Python-2.7.4/bin:/usr/bin:/bin:/sbin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/usr/local/java/bin/
util=$(cd "$(dirname "$0")"; pwd)/nosql_mut_util.sh

LANG=C

IP=$(/sbin/ifconfig|grep -b1 "eth0"|grep "inet addr"|awk -F':' '{print $2}'|awk '{print $1}'|grep -vE '172\.16\.|127\.|192\.|10\.'| head -1)

REDIS_ARRAY=`ls /etc/snmp/yyms_agent_redis_scripts/redis_[0-9]*.conf|awk -F "/" '{print $NF}'|awk -F "." '{print $1}'|awk -F "_" '{print $2}'`

for REDIS_PORT in $REDIS_ARRAY
do
    eval ETC_FILE=/etc/snmp/yyms_agent_redis_scripts/redis_$REDIS_PORT.conf
    eval $(sed 's/ //g;/=/!d' < $ETC_FILE)
    if [[  "X${REDIS_PORT}"  !=  "X${port}"  ]];then
           port=${REDIS_PORT}
           msg="redis_${port}_etc_error"
           msg=$(echo $msg|sed 's/ /_/g')
           /home/dspeak/yyms/yymp/yymp_report_script/yymp_report_alarm.py "id=13007&sid=79923&alarm_level=3&pre=0&port=$port&msg='$msg'&pname=redis&op_admin_dw=${operator_dw}&op_admin=${operator}&buss_name=$business_model"
           bash ${util} ${port} 3  13007 ${msg}
    fi
    cache_file=/tmp/.${port}_$(basename $0).clients.$(date +%Y%m%d%H%M%S)

    ALIVE=`/usr/bin/redis-cli -p $port ping`
    if [[ $? -ne 0 ||  "x$ALIVE" != "xPONG" ]] ; then
       count=0
       for i in $(seq 5)
       do
            ALIVE=`/usr/bin/redis-cli -p $port ping`
            [[ $? -ne 0 ||  "x$ALIVE" != "xPONG" ]] && count=$(( $count + 1 ))
            sleep 0.2

       done
       if [ $count -eq 5 ];then
           if [[ "X$ALIVE"  =~  "reach" ]];then
               cmd="ss -t -a -n  -o state  established '( sport = :${port} )'"
               eval $cmd  > ${cache_file}
               #msg="port:$port;status:$ALIVE (MAXCONN:$(cat /data/redis_${port}/redis${port}.conf | grep -ioP "maxclients[\s]+[0-9]+" | awk '{print $2}'))"
               msg="redis_${port}_alive[maxclients_reached[MAXCONN:$(cat /data/redis_${port}/redis${port}.conf | grep -ioP "maxclients[\s]+[0-9]+" | awk '{print $2}')]]"
               msg=$(echo $msg|sed 's/ /_/g')
               /home/dspeak/yyms/yymp/yymp_report_script/yymp_report_alarm.py "id=13007&sid=79923&alarm_level=2&pre=0&port=$port&msg='$msg'&pname=redis&op_admin_dw=${developer_dw}&op_admin=${developer}&buss_name=$business_model"
               bash ${util} ${port} 2  13007 ${msg}
               unset cmd
               continue
           else
               if [[ $(ss -l -n -t -4 | grep "*:${port} " | wc -l) -eq 1 ]];then
                  #msg="port:$port;实例堵塞导致存活探测失败"
                  msg="redis_${port}_alive_probe_failure"
                  msg=$(echo $msg|sed 's/ /_/g')
                  /home/dspeak/yyms/yymp/yymp_report_script/yymp_report_alarm.py "id=13007&sid=79923&alarm_level=3&pre=0&port=$port&msg='$msg'&pname=redis&op_admin_dw=${operator_dw}&op_admin=$operator&buss_name=$business_model"
                  bash ${util} ${port} 3  13007 ${msg}
                  continue
               else
                  #msg="port:$port;status:down"
                  msg="redis_${port}_alive_down"
                  msg=$(echo $msg|sed 's/ /_/g')
                  /home/dspeak/yyms/yymp/yymp_report_script/yymp_report_alarm.py "id=13007&sid=79923&alarm_level=2&pre=0&port=$port&msg='$msg'&pname=redis&op_admin_dw=${operator_dw}&op_admin=$operator&buss_name=$business_model"
                  bash ${util} ${port} 2  13007 ${msg}
                  continue
               fi
           fi
       fi
    fi

    [[ ${port:0:1} -eq 2  ]] && continue

    PID_FILE=`/usr/bin/redis-cli -p $port config get pidfile | xargs | awk '{print $2}' | tr -d '"'`
    [[ ! -z $PID_FILE  &&  -f $PID_FILE  &&  -s $PID_FILE ]] && PID=`cat ${PID_FILE}` || continue

    [[ $(/usr/bin/redis-cli -p $port info replication | grep master_link_status)  =~ master_link_status:([[:alpha:].]+) ]] && MASTER_SLAVE_LINK_STATUS=${BASH_REMATCH[1]} || MASTER_SLAVE_LINK_STATUS=''
    [[ $(/usr/bin/redis-cli -p $port info replication | grep "^master_host:")  =~ master_host:(.*) ]] && MASTER_HOST=`echo ${BASH_REMATCH[1]} | tr -d '\r' | tr -d '\n' ` || MASTER_HOST=''
    [[ $(/usr/bin/redis-cli -p $port info replication | grep "^master_port:")  =~ master_port:([[:digit:].]+) ]] && MASTER_PORT=${BASH_REMATCH[1]} || MASTER_PORT=''

    if [ "X$MASTER_SLAVE_LINK_STATUS" = "Xdown" ];then
       counter=0
       for i in $(seq 5)
       do
           [[ $(/usr/bin/redis-cli -p $port info replication | grep master_link_status)  =~ master_link_status:([[:alpha:].]+) ]] && MASTER_SLAVE_LINK_STATUS=${BASH_REMATCH[1]} || MASTER_SLAVE_LINK_STATUS=''
           [ "X$MASTER_SLAVE_LINK_STATUS" = "Xdown" ] && counter=$(( $counter + 1 ))
           sleep 0.2
       done
           if [ $counter -eq 5 ];then
                #msg="slave[$IP:$port] -> master[$MASTER_HOST:$MASTER_PORT];status:master_link_status  down"
                #msg="redis_${port}_master_link_status[down][m:[$MASTER_HOST:$MASTER_PORT]]"
                msg="redis_${port}_主从同步堵塞导致数据库延迟[网络原因居多]"
                python /home/dspeak/yyms/yymp/yymp_report_script/yymp_report_alarm.py "id=13597&sid=82191&alarm_level=2&pre=0&port=$port&msg='$msg'&pname=redis&pid=$PID&op_admin_dw=${developer_dw}&op_admin=$developer&buss_name=$business_model"
                bash ${util} ${port} 2  13597 ${msg}
           fi
    fi


done