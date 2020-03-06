#!/bin/bash
#停止同步脚本，或停止redis-shake同步


porta=$1
source_string=$2

###检查readlog脚本是否已经终止#####
function check_start_status(){
porta=$1
source_string=$2
check_pre_check=`ps -ef | grep redis_shake_precheck |grep -w $source_string | grep -v "grep" | wc -l`
if [[  $check_pre_check -ge 1 ]];then

     echo "checking has not finished, can not stop"
     echo "return  executed failed"
     msg="return  executed failed"
     echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
     exit


fi

check_readlog=`ps -ef | grep redis_shake_readlog |grep -w $porta| grep -v "grep" | wc -l`
redlog_pid=`ps -ef | grep redis_shake_readlog |grep -w $porta| grep -v "grep"  | awk '{print $2}'`
if [[  $check_readlog -ge 1 ]];then

     sudo kill -9 $redlog_pid
     fi
 stop_sync  $porta


}

###停掉redis-shake进程#####
function stop_sync(){
porta=$1
        #sudo ps -ef | grep "redis-shake" | grep "${porta}"| grep -v "grep" | grep -v "redis_shake_stop"
check_shake=`ps -ef | grep "redis-shake" | grep "${porta}"| grep -v "grep" | grep -v "redis_shake_stop"| wc -l`
if [[  $check_shake  -eq  1  ]];then

     shake_pid=`ps -ef | grep "redis-shake" | grep -v "grep" | grep "${porta}" | grep -v "redis_shake_stop"|grep -v "startpro" | awk '{print $2}'`
     shake_file_pid=`cat /data/redis-shake/redis-shake-${porta}/redis-shake${porta}.pid`
     if [[ $shake_pid -eq $shake_file_pid ]]; then
     shake_log=/data/dbyyms/redis/.redis-shake.log
  	sed -i '/^'$porta'/d' $shake_log
		 sudo kill -9 $shake_pid

           echo `date +'%Y-%m-%d %H:%M:%S'` ":" "kill redis-shake successfully"
           msg="return  executed success"
           echo $(eval echo '{\"code\": 0,\"msg\": \""$msg"\" }' )| python -m json.tool
     else
      echo `date +'%Y-%m-%d %H:%M:%S'` ":" "redis-shake process PID is not equal to PID file PID, please check manually" 
      msg="return  executed failed"
      echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool     
     fi
else
    echo `date +'%Y-%m-%d %H:%M:%S'` ":" "redis-shake process does not exist"
    msg="return  executed failed"
    echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
    exit
 fi
}
check_start_status  $porta  $source_string
