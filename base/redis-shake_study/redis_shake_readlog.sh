#!/bin/bash

#log_file=/data/redis-shake/redis-shake-9318/sync.log.timestamp

porta=$1
log_file=$2
function read_log(){

sync_conf_file=/data/redis-shake/redis-shake-${porta}/redis-shake${porta}.conf
source_num=`cat $sync_conf_file | grep "source.address" | awk -F "=" '{print $2}' |awk  '{s+=gsub(/:/,"&")}END{print s}'`

if [[ ! -f ${sync_conf_file}  ]];then
echo `date +'%Y-%m-%d %H:%M:%S'`: "ERROR" "sync config file doesn't exists ..."
msg="return  executed failed"
echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
fi


sleep 5
 while :
     do
     read  error_count <<< $(   awk 'BEGIN{IGNORECASE=1; error_count=0}     /error|crash|ERR|err|fail/{error_count+=1}      END{print error_count}'  ${log_file}    )
     if [[  $error_count -ge 1  ]];then
        error_info=`date +'%Y-%m-%d %H:%M:%S'`+": "+`cat ${log_file} | grep -w "\[error\]"`
        echo $error_info
        msg="return  executed failed"
		echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
        break
        fi
     sync_flag=`grep -w "dbSyncer\[[0-9]\]"  ${log_file} | grep "%"| wc -l`
     if [[ $sync_flag -ge 1 ]]; then

     echo `date +'%Y-%m-%d %H:%M:%S'`: "source redis and target redis are syncing"
     break
     fi
     sleep 5
     done
 while :
     do
     read  error_count <<< $(   awk 'BEGIN{IGNORECASE=1; error_count=0}     /error|crash|ERR|err|fail/{error_count+=1}      END{print error_count}'  ${log_file}    )
     if [[  $error_count -ge 1  ]];then
        error_info=`date +'%Y-%m-%d %H:%M:%S'`+":"+`cat ${log_file} | grep -w "\[error\]"`
        echo $error_info
        msg="return  executed failed"
		echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
        break
        fi
     is_done=`grep "sync rdb done" ${log_file} | wc -l`
     is_full=`grep "100%" ${log_file}| wc -l`
     if [[  $is_done -eq  $source_num ]] || [[  $is_full  -eq  $source_num  ]];then
         echo `date +'%Y-%m-%d %H:%M:%S'`: "sync rdb done"
         msg="return  executed success"
		 echo $(eval echo '{\"code\": 0,\"msg\": \""$msg"\" }' )| python -m json.tool
		 echo $porta":start" >> /data/dbyyms/redis/.redis-shake.log
         break
         fi

     sleep 5
     done
}
read_log
