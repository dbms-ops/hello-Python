#!/bin/bash
porta=$1
function start_sync(){
sync_conf_file=/data/redis-shake/redis-shake-${porta}/redis-shake${porta}.conf
if [[ ! -f ${sync_conf_file}  ]];then
echo `date +'%Y-%m-%d %H:%M:%S'`: "ERROR" "sync config file doesn't exists ..."
msg="return  executed failed"
echo $(eval echo '{\"code\": 1,\"msg\": \""$msg"\" }' )| python -m json.tool
fi
/data/redis-shake/redis-shake-${porta}/redis-shake.linux -type=sync -conf=${sync_conf_file} > /dev/null
}
start_sync
