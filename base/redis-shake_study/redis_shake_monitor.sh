#!/bin/bash

function push_alarm(){


    local AlarmLevel=$1
    local id=$2
    local sid=$3

    if [[ $AlarmLevel -gt 0 ]]
    then

            msg="redis_shake_pro_stop_abnormally_$porta"
            msg=$(echo $msg | sed 's/ /_/g')
            port=`cat /data/redis-shake/redis-shake-$porta/redis-shake$porta.conf | grep target.address | awk -F ":" '{print $2}'  | awk -F ";" '{print $1}'`
            eval ETC_FILE=/etc/snmp/yyms_agent_redis_scripts/redis_$port.conf
            eval $(sed 's/ //g;/=/!d' < $ETC_FILE)
            python /home/dspeak/yyms/yymp/yymp_report_script/yymp_report_alarm.py "id=$id&sid=$sid&pre=0&port=${port}&alarm_level=$AlarmLevel&msg=$msg&pname=redis&op_admin_dw=$operator_dw&op_admin=$operator&buss_name=$business_model"

    fi
}

shake_log=/data/dbyyms/redis/.redis-shake.log
if [ -f $shake_log ]
then
 num=`cat $shake_log | grep start | wc -l`
 if [ $num  -eq 1 ]
  then 
   porta=`cat $shake_log | grep start | awk -F ":" '{print $1}'`
   sudo ps -ef | grep "redis-shake" | grep -v "grep" | grep "${porta}" | grep -v "redis_shake_stop"|grep -v "startpro"
   [ $? -ne 0 ] && push_alarm 2 45300 146613 && sed -i '/^'$porta'/d' $shake_log
 elif [ $num -gt 1 ]
   then
   for porta in `cat $shake_log | grep start | awk -F ":" '{print $1}'`
   do
    ps -ef | grep "redis-shake" | grep -v "grep" | grep "${porta}" | grep -v "redis_shake_stop"|grep -v "startpro"
    [ $? -ne 0 ] && push_alarm 2 45300 146613  && sed -i '/^'$porta'/d' $shake_log
    done
    
fi
fi
