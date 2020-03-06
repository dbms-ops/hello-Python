#!/bin/bash
#检查主库状态，安装redis-shake
source_string=$1
target_string=$2
source_type=$3
target_type=$4

######获取shake端口######
function get_shake_port(){

[[  -d /data/redis-shake ]] || mkdir -p /data/redis-shake  

cd /data/redis-shake  

 confnum=`ls /data/redis-shake |  grep -P 'redis-shake-\d{4}' | wc -l`
     if [[ $confnum -eq 0 ]]; then 
     PORT_COUNT=0
     else 
    PORT_COUNT=`ls /data/redis-shake | grep -P 'redis-shake-\d{4}' | wc -l`
    fi
 
 
porta=`echo $PORT_COUNT+9310 | bc`
portb=`echo $PORT_COUNT+9620 | bc`

echo `date +'%Y-%m-%d %H:%M:%S'`: "allocate shake port $porta finished."
}


######检查源库状态######
function check_source_status(){
source_ip=$1
source_port=$2

echo `date +'%Y-%m-%d %H:%M:%S'`: "start to check $source_ip:$source_port status"
rolecheck=`redis-cli -h $source_ip -p $source_port info replication | grep role | awk -F ":" '{print $2}'| sed -e 's/\r//g'`
rdbcheck=`redis-cli -h $source_ip -p $source_port config get rdbchecksum |xargs| awk '{print $2}'| sed -e 's/\r//g'`

if [[ "X$rolecheck" == "Xmaster" ]]
   then
   connected_slaves=`redis-cli -h $source_ip -p $source_port info replication | grep connected_slaves| awk -F ":" '{print $2}' | sed -e 's/\r//g'`
   if [[ $connected_slaves -eq 1 ]]
      then
      echo `date +'%Y-%m-%d %H:%M:%S'`: "source ip,port is a master with slaves"
      msg="return  executed failed"
      echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
      exit
   elif [[ $connected_slaves -eq 0 ]] && [[ "X$rdbcheck" == "Xyes"  ]]
       then
      echo `date +'%Y-%m-%d %H:%M:%S'`: "source ip,port is a single master, and rdbchecksum yes"
   elif [[ $connected_slaves -eq 0 ]] && [[ "X$rdbcheck" == "Xno"   ]]
       then
       echo `date +'%Y-%m-%d %H:%M:%S'`: "source ip,port is a single master, and rdbchecksum no"
	   msg="return  executed failed"
       echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
       exit
    fi

elif [[  "X$rolecheck" == "Xslave"  ]]
   then
   if [[ "X$rdbcheck" == "Xyes" ]]
     then
     echo `date +'%Y-%m-%d %H:%M:%S'`: "source ip,port is a slave, and rdbchecksum yes"
   elif [[ "X$rdbcheck" == "Xno" ]]
     then
     echo `date +'%Y-%m-%d %H:%M:%S'`: "source ip,port is a slave, and rdbchecksum no"
     msg="return  executed failed"
	 echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
     exit
   fi
else


echo  `date +'%Y-%m-%d %H:%M:%S'`: "Could not connect to Redis at $source_ip:$source_port"
msg="return  executed failed"
echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
exit
fi

}

######检查standalone-standalone内存状态######
function check_ss_memory(){
source_ip=$1
source_port=$2
target_ip=$3
target_port=$4
echo `date +'%Y-%m-%d %H:%M:%S'`: "start to check source and target redis memory"
source_memory=`redis-cli -h $source_ip -p $source_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
target_memory=`redis-cli -h $target_ip -p $target_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
target_max=`redis-cli -h $target_ip -p $target_port config get maxmemory  | xargs| awk '{print $2}' | sed -e 's/\r//g'`
target_ava=`echo $target_max-$target_memory |bc`
if [[  $target_ava -lt $(($source_memory-100000000))  ]]
then 
   echo `date +'%Y-%m-%d %H:%M:%S'`: "target redis has not free memory to load keys from source redis"
   msg="return  executed failed"
   echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
exit
else
   echo `date +'%Y-%m-%d %H:%M:%S'`: "check $target_ip:$target_port memory success"
fi

}

######检查standalone-cluster内存状态######
function check_sc_memory(){
source_ip=$1
source_port=$2
target_string=$3
echo `date +'%Y-%m-%d %H:%M:%S'`: "start to check source and target redis memory"
source_memory=`redis-cli -h $source_ip -p $source_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
cluster_info=cluster_info_`date +%s`
cluster_info_dir=/data/dba_logs/redis_shake_target_cluster
 
   [ ! -d ${cluster_info_dir} ] && mkdir -p ${cluster_info_dir}
   doc=${cluster_info_dir}/${cluster_info}
   echo $target_string > $doc
   sed -i 's/;/\n/g' $doc
   sed -i 's/:/ /g' $doc

   sc=`cat $doc| wc -l`
   i=1
   target_ava_all=0
   for ID in `cat $doc`
   do
     NUM=$i
     if [[ $NUM -gt $sc  ]]
      then
       continue
     else
      target_ip=$(awk 'NR=='$NUM' {print $1}' $doc)
      target_port=$(awk 'NR=='$NUM' {print $2}' $doc)
      target_memory=`redis-cli -h $target_ip -p $target_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
      target_max=`redis-cli -h $target_ip -p $target_port config get maxmemory  | xargs| awk '{print $2}' | sed -e 's/\r//g'`
      target_ava=`echo $target_max-$target_memory |bc`
      target_ava_all=`echo $target_ava_all+$target_ava|bc`
      
      i=`echo $i+1 | bc`
      fi
done
if [[  $target_ava_all -lt $(($source_memory-100000000))  ]]
then 
   echo `date +'%Y-%m-%d %H:%M:%S'`: "target redis has not free memory to load keys from source redis"
   msg="return  executed failed"
   echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
exit
else
   echo `date +'%Y-%m-%d %H:%M:%S'`: "check target redis cluster memory success"
fi

}

######检查cluster-standalone内存状态######
function check_cs_memory(){
source_string=$1
target_ip=$2
target_port=$3
echo `date +'%Y-%m-%d %H:%M:%S'`: "start to check source and target redis memory"
cluster_info=cluster_info_`date +%s`
cluster_info_dir=/data/dba_logs/redis_shake_source_cluster
 
   [ ! -d ${cluster_info_dir} ] && mkdir -p ${cluster_info_dir}
   doc=${cluster_info_dir}/${cluster_info}
   echo $source_string > $doc
   sed -i 's/;/\n/g' $doc
   sed -i 's/:/ /g' $doc

   sc=`cat $doc| wc -l`
   i=1
   source_mem_all=0
   for ID in `cat $doc`
   do
     NUM=$i
     if [[ $NUM -gt $sc  ]]
      then
       continue
     else
      source_ip=$(awk 'NR=='$NUM' {print $1}' $doc)
      source_port=$(awk 'NR=='$NUM' {print $2}' $doc)
      source_memory=`redis-cli -h $source_ip -p $source_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
      
      source_mem_all=`echo $source_mem_all+$source_memory|bc`
      
      i=`echo $i+1 | bc`
      fi
done
      target_memory=`redis-cli -h $target_ip -p $target_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
      target_max=`redis-cli -h $target_ip -p $target_port config get maxmemory  | xargs| awk '{print $2}' | sed -e 's/\r//g'`
      target_ava=`echo $target_max-$target_memory |bc`
if [[  $target_ava -lt $(($source_mem_all-100000000))  ]]
then 
   echo `date +'%Y-%m-%d %H:%M:%S'`: "target redis has not free memory to load keys from source redis"
   msg="return  executed failed"
   echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
exit
else
   echo `date +'%Y-%m-%d %H:%M:%S'`: "check target redis cluster memory success"
fi

}


######检查cluster-cluster内存状态######
function check_cc_memory(){
source_string=$1
target_string=$2
echo `date +'%Y-%m-%d %H:%M:%S'`: "start to check source and target redis memory"
cluster_info=cluster_info_`date +%s`
cluster_info_dir=/data/dba_logs/redis_shake_source_cluster
 
   [ ! -d ${cluster_info_dir} ] && mkdir -p ${cluster_info_dir}
   doc=${cluster_info_dir}/${cluster_info}
   echo $source_string > $doc
   sed -i 's/;/\n/g' $doc
   sed -i 's/:/ /g' $doc

   sc=`cat $doc| wc -l`
   i=1
   source_mem_all=0
   for ID in `cat $doc`
   do
     NUM=$i
     if [[ $NUM -gt $sc  ]]
      then
       continue
     else
      source_ip=$(awk 'NR=='$NUM' {print $1}' $doc)
      source_port=$(awk 'NR=='$NUM' {print $2}' $doc)
      source_memory=`redis-cli -h $source_ip -p $source_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
      
      source_mem_all=`echo $source_mem_all+$source_memory|bc`
      
      i=`echo $i+1 | bc`
      fi
done
cluster_new_info=cluster_info_`date +%s`
cluster_new_info_dir=/data/dba_logs/redis_shake_target_cluster
  [ ! -d ${cluster_new_info_dir} ] && mkdir -p ${cluster_new_info_dir}
   doc=${cluster_new_info_dir}/${cluster_new_info}
   echo $target_string > $doc
   sed -i 's/;/\n/g' $doc
   sed -i 's/:/ /g' $doc

   sc=`cat $doc| wc -l`
   i=1
   target_ava_all=0
   for ID in `cat $doc`
   do
     NUM=$i
     if [[ $NUM -gt $sc  ]]
      then
       continue
     else
      target_ip=$(awk 'NR=='$NUM' {print $1}' $doc)
      target_port=$(awk 'NR=='$NUM' {print $2}' $doc)
      target_memory=`redis-cli -h $target_ip -p $target_port info memory | grep -w "used_memory" | awk -F ":" '{print $2}' | sed -e 's/\r//g'`
      target_max=`redis-cli -h $target_ip -p $target_port config get maxmemory  | xargs| awk '{print $2}' | sed -e 's/\r//g'`
      target_ava=`echo $target_max-$target_memory |bc`
      target_ava_all=`echo $target_ava_all+$target_ava|bc`
      
      i=`echo $i+1 | bc`
      fi
done

if [[  $target_ava_all -lt $(($source_mem_all-100000000))  ]]
then 
   echo `date +'%Y-%m-%d %H:%M:%S'`: "target redis has not free memory to load keys from source redis"
   msg="return  executed failed"
   echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
exit
else
   echo `date +'%Y-%m-%d %H:%M:%S'`: "check target redis cluster memory success"
fi

}

######下载######
function download(){

    echo  `date +'%Y-%m-%d %H:%M:%S'`: "begin to download redis-shake.tar.gz"
    [ -f /tmp/redis-shake.tar.gz ] &&  cd /tmp/  && rm -rf redis-shake.tar.gz
    [ -f /tmp/redis-shake.tar.gz.md5 ] &&  cd /tmp/  && rm -rf redis-shake.tar.gz.md5

    wget -O /tmp/redis-shake.tar.gz      "http://dbms.sysop.duowan.com/public/downloadFile/?fileType=redis&fileName=redis-shake.tar.gz"                 2>/dev/null
    wget -O /tmp/redis-shake.tar.gz.md5  "http://dbms.sysop.duowan.com/public/downloadFile/?fileType=redis&fileName=redis-shake.tar.gz.md5"             2>/dev/null


    if [[ ! -s /tmp/redis-shake.tar.gz  ||  ! -s /tmp/redis-shake.tar.gz.md5   ]];then
        echo  `date +'%Y-%m-%d %H:%M:%S'`: "ERROR" "wget redis-shake.tar.gz fail"
        msg="return  executed failed"
		echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
        #echo   "{'code':-1,'msg':'wget redis-shake.tar.gz fail'}" 
        exit 0
    fi
    if [[ "X$(md5sum /tmp/redis-shake.tar.gz | awk '{print $1}' |tr -d ' ')" != "X$(cat /tmp/redis-shake.tar.gz.md5 | tr -d ' ')" ]];then
        echo `date +'%Y-%m-%d %H:%M:%S'`:  "ERROR" "redis-shake.tar.gz md5 error"
        echo `date +'%Y-%m-%d %H:%M:%S'`: "ERROR" "exit ..."
        #echo   "{'code':-1,'msg':'redis-shake.tar.gz md5 error'}" 
        msg="return  executed failed"
		echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
        exit 0
    fi

    echo `date +'%Y-%m-%d %H:%M:%S'`: "end to download redis-shake.tar.gz"
}

######获取资源######
function getResource(){
   filename=redis-shake.tar.gz
   [[  -d /data/redis-shake-pkg  ]] || mkdir -p /data/redis-shake-pkg
   if [[ ! -f /data/redis-shake-pkg/${filename}  ]];then
        download 
        alias cp=cp
        cp -rf /tmp/${filename}  /data/redis-shake-pkg/
   else
        cp -rf /data/redis-shake-pkg/${filename}  /tmp/
         wget -O /tmp/redis-shake.tar.gz.md5  "http://dbms.sysop.duowan.com/public/downloadFile/?fileType=redis&fileName=redis-shake.tar.gz.md5"             2>/dev/null
        if [[ "X$(md5sum /tmp/redis-shake.tar.gz | awk '{print $1}' |tr -d ' ')" != "X$(cat /tmp/redis-shake.tar.gz.md5 | tr -d ' ')" ]];then
            download  
            alias cp=cp
            cp -rf /tmp/${filename}  /data/redis-shake-pkg/
        fi


   fi

}

######安装redis-shake######
function install_shake(){

porta=$1

#./redis-shake -type=sync -conf=redis-shake.conf 
echo `date +'%Y-%m-%d %H:%M:%S'`: "start to install redis-shake in target redis server"
cd /data/redis-shake-pkg
if [[ ! -f  redis-shake.linux ]] || [[  ! -f redis-shake.conf ]] ; then
    tar -zxf redis-shake.tar.gz
    fi

[[ ! -d /data/redis-shake/redis-shake-${porta}/  ]]  && mkdir -p /data/redis-shake/redis-shake-${porta}/

log_file=/data/redis-shake/redis-shake-${porta}/sync.log.`date +%s`
pid_path=/data/redis-shake/redis-shake-${porta}
sync_conf_file=/data/redis-shake/redis-shake-${porta}/redis-shake${porta}.conf

cp -f /data/redis-shake-pkg/redis-shake.conf /data/redis-shake/redis-shake-${porta}/redis-shake${porta}.conf
cp -f /data/redis-shake-pkg/redis-shake.linux    /data/redis-shake/redis-shake-${porta}/redis-shake.linux

sed -i 's/redis-shake/redis-shake'${porta}'/g' ${sync_conf_file}

sed -i 's/system_profile = 9310/system_profile = '${porta}'/g' ${sync_conf_file}
sed -i 's/http_profile = 9320/http_profile = '${portb}'/g' ${sync_conf_file}

sed -i 's/127.0.0.1:20441/'${source_string}'/g' ${sync_conf_file}
sed -i 's/127.0.0.1:20551/'${target_string}'/g' ${sync_conf_file}

sed -i "s#pid_path =#pid_path =${pid_path}#"  ${sync_conf_file}
sed -i "s#log.file =#log.file =${log_file}#"  ${sync_conf_file}

if [[ "X$source_type" == "Xcluster" ]]
   then 
    sed -i 's/source.type = standalone/source.type ='${source_type}'/g' ${sync_conf_file}
    sed -i 's/source.rdb.parallel = 0/source.rdb.parallel = 1/g' ${sync_conf_file}
fi
if [[ "X$target_type" == "Xcluster" ]]
   then 
    sed -i 's/target.type = standalone/target.type ='${target_type}'/g' ${sync_conf_file}
fi

porta_count=`cat /usr/local/virus/iptables/iptables.add | grep ${porta} | grep "DROP" | wc -l`
portb_count=`cat /usr/local/virus/iptables/iptables.add | grep ${portb} | grep "DROP" | wc -l`
echo `date +'%Y-%m-%d %H:%M:%S'`: "start to add system_profile port ,http_profile port to iptables"
if [[  $porta_count -eq 0  ]];then
    echo "iptables -A INPUT -p tcp -m multiport --dport ${porta} -j DROP " >>  /usr/local/virus/iptables/iptables.add 
fi
if [[  $portb_count -eq 0  ]];then
    echo "iptables -A INPUT -p tcp -m multiport --dport ${portb} -j DROP " >>  /usr/local/virus/iptables/iptables.add 
fi

bash /usr/local/virus/iptables/iptables.sh > /dev/null  
[[ $? -ne 0 ]]  && echo `date +'%Y-%m-%d %H:%M:%S'`: "flush system_profile port ,http_profile port iptables failed" && exit  && echo  $(eval echo '{\"code\": 1,\"msg\": \"return  executed failed\" }' )| python -m json.tool
echo `date +'%Y-%m-%d %H:%M:%S'`: "add system_profile port ,http_profile port to iptables success "
echo `date +'%Y-%m-%d %H:%M:%S'`: "finished install"
echo `date +'%Y-%m-%d %H:%M:%S'`: "log in " $log_file
msg="return executed success"
echo $(eval echo '{\"code\": 0,\"msg\": \""$msg"\",\"data\": \""$log_file"\",\"port\": \""$porta"\" }' )| python -m json.tool
 

}

############主程序###########

get_shake_port

if [[ "X$source_type" != "Xcluster" ]]
  then
  source_ip=`echo $source_string| awk -F ":" '{print $1}'`
  source_port=`echo $source_string| awk -F ":" '{print $2}'`
  check_source_status  $source_ip  $source_port
else
   cluster_info=cluster_info_`date +%s`
   cluster_info_dir=/data/dba_logs/redis_shake_source_cluster
 
   [ ! -d ${cluster_info_dir} ] && mkdir -p ${cluster_info_dir}
   doc=${cluster_info_dir}/${cluster_info}
   echo $source_string > $doc
   sed -i 's/;/\n/g' $doc
   sed -i 's/:/ /g' $doc

   sc=`cat $doc| wc -l`
   i=1
   for ID in `cat $doc`
   do
     NUM=$i
     if [[ $NUM -gt $sc  ]]
      then
       continue
     else
      source_ip=$(awk 'NR=='$NUM' {print $1}' $doc)
      source_port=$(awk 'NR=='$NUM' {print $2}' $doc)
      check_source_status  $source_ip  $source_port
      i=`echo $i+1 | bc`
      fi
done
fi

if [[ "X$source_type" != "Xcluster" ]] &&  [[ "X$target_type" != "Xcluster" ]]
then
  source_ip=`echo $source_string| awk -F ":" '{print $1}'`
  source_port=`echo $source_string| awk -F ":" '{print $2}'`
  target_ip=`echo $target_string| awk -F ":" '{print $1}'`
  target_port=`echo $target_string| awk -F ":" '{print $2}'`
  check_ss_memory   $source_ip  $source_port  $target_ip  $target_port
elif [[ "X$source_type" != "Xcluster" ]] &&  [[ "X$target_type" == "Xcluster" ]]
then
  source_ip=`echo $source_string| awk -F ":" '{print $1}'`
  source_port=`echo $source_string| awk -F ":" '{print $2}'`
  check_sc_memory $source_ip $source_port $target_string
  
elif [[ "X$source_type" == "Xcluster" ]] &&  [[ "X$target_type" != "Xcluster" ]]
then
    target_ip=`echo $target_string| awk -F ":" '{print $1}'`
    target_port=`echo $target_string| awk -F ":" '{print $2}'`
    check_cs_memory $source_string   $target_ip  $target_port
    
elif [[ "X$source_type" == "Xcluster" ]] &&  [[ "X$target_type" == "Xcluster" ]]
then 
    check_cc_memory $source_string  $target_string
fi


getResource
install_shake $porta

