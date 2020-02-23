#!/usr/bin/env bash
#!/bin/bash
# 通过配置文件快速登录mysql的小工具
export PS4='${LINENO}: '

function prepare() {
    port=$1
    if [[ -f $port ]]
    then
        conf=$port
    else
        conf=/etc/snmp/yyms_agent_db_scripts/db_$port.conf
    fi

    if [[ -f $conf ]]
    then
        eval $(sed 's/ //g;s/>//g;/=/!d' $conf)
    else
        echo "$conf not exists" 1>&2
        exit 1
    fi

    if [[ -f /usr/local/mysql_$port/bin/mysqladmin ]]
    then
        MySQL=/usr/local/mysql_$port/bin/mysql
        ADM=/usr/local/mysql_$port/bin/mysqladmin
    else
        MySQL=mysql
        ADM=mysqladmin
    fi
}

function event() {
    [[ -f /home/dspeak/yyms/yyms_report/yyms_report_elog ]] || return
    if [[ -n $port ]]
    then
        json="{\"log_level\":3, \"log_type\":\"mysql\", \"sub_type\":$1, \"content\":\"$2\", \"extra\": { \"port\":\"$port\",\"business_model\":\"$business_model\",\"dev_master\":\"$developer\",\"op_master\":\"$operator\",\"business\":\"$business_name\"}}"
        /home/dspeak/yyms/yyms_report/yyms_report_elog -m "$json"
    fi

}

function query() {
    $MySQL -A -h0 -P $port -u $user -p$password "$@" 2>/dev/null || exit 1
}

function log() {
    # 记录错误日志
    if [[ -f /usr/local/bin/record ]]
    then
        /usr/local/bin/record -l info -f $logfile -m "$*"
    fi
}

function status() {
        if [[ -n $1 ]]
        then
                port=$1
        else
                return 1
        fi
        prepare $port
        logfile=log_status_$port
        datetime="$(date '+# Time %F %T')"
        # sql="select ID,USER,HOST,DB,COMMAND,TIME,STATE,INFO from information_schema.processlist where info not in ('NULL') and db not in ('information_schema') order by time desc\G"
        # log "### mysqld $port running processlist:"
        # log "$(query -e "$sql")"
        # sql="select b.user, b.host, b.db, b.command, b.time, b.state, a.*  from information_schema.innodb_trx a join information_schema.processlist b on a.trx_mysql_thread_id=b.id order by a.trx_started desc\G"
        sql="SELECT r.trx_id as locked_trx, r.trx_query as locked_sql, b.trx_id as block_id, b.trx_query as block_sql, b.trx_mysql_thread_id as block_thread, b.trx_started as block_start_time FROM(information_schema.innodb_lock_waits w INNER JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id) INNER JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id order by b.trx_started desc\G"
        log "### mysqld $port deadlock:"
        query -e "$sql" >> $logfile
        performance=$( query -Ne "select @@performance_schema")
        if [[ $performance -eq 1 ]]
        then
             sql="select trx.trx_mysql_thread_id thread_id, prl.host, prl.user, trx.trx_id, trx.trx_started, prl.time, prl.db current_db, trx.trx_query current_sql, trx.trx_state, thd.processlist_command command, last.current_schema last_db, last.sql_text last_sql from information_schema.innodb_trx trx straight_join performance_schema.threads thd on trx.trx_mysql_thread_id=thd.processlist_id straight_join performance_schema.events_statements_current last on thd.thread_id = last.thread_id straight_join information_schema.processlist prl on trx.trx_mysql_thread_id = prl.id where trx_state='running' and command='sleep' order by trx.trx_started\G"
                else
            sql="select prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, prl.state, trx.trx_state, trx.trx_query from information_schema.innodb_trx trx straight_join information_schema.processlist prl on trx.trx_mysql_thread_id=prl.id where prl.command='Sleep' and trx.trx_state='RUNNING' order by trx.trx_started\G"
        fi
        log "### mysqld $port uncommitted:"
        query -e "$sql" >> $logfile
        sql="select prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, prl.state, trx.trx_state, trx.trx_query
        from information_schema.innodb_trx trx straight_join information_schema.processlist prl on trx.trx_mysql_thread_id=prl.id order by trx.trx_started desc\G"
        log "### mysqld $port transaction:"
        query -e "$sql" >> $logfile
        log "### mysqld $port innodb status:"
        sql="show engine innodb status\G"
        query -e "$sql" >> $logfile
        echo "    日志已记录到当前目录下的文件 log_status_$port
        deadlock            死锁事务
        uncommitted         未提交事务
        transaction         当前事务
        innodb status       show engine innodb status
        "
}

function qps() {
    port=$1
    while true
    do
        read delete insert select update uptime <<< $(/usr/local/bin/lg $port -Ne 'show global status where Variable_name in ("Com_select","Com_insert"
    ,"Com_update","Com_delete","Uptime")' 2>/dev/null | awk '{print $2}' | xargs)
        if [[ $[n%10] -gt 0 ]]
        then
            period=$[uptime - last_uptime]
            qps_delete=$[(delete - last_delete)/period]
            qps_insert=$[(insert - last_insert)/period]
            qps_update=$[(update - last_update)/period]
            qps_select=$[(select - last_select)/period]
            qps=$[qps_delete+qps_insert+qps_update+qps_select]
            printf "%9d %6d %6d %6d %6d\n" $qps $qps_select $qps_insert $qps_update $qps_delete
        else
            echo "|---QPS---|select insert update delete|"
        fi
        last_uptime=$uptime
        last_delete=$delete
        last_select=$select
        last_update=$update
        last_insert=$insert
        n=$[n+1]
        sleep 2
    done
}

function kill() {
    port=$1
    case $2 in
        sleep)
            sql="select id from information_schema.processlist where command='Sleep' and user not in ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', 'unauthenticated', 'ping')"
            ;;
        idle)
            sql="select prl.id from information_schema.innodb_trx trx straight_join information_schema.processlist prl on trx.trx_mysql_thread_id=prl.id where prl.command='Sleep' and trx.trx_state='RUNNING' order by trx.trx_started"
            ;;
        run)
            sql="select id from information_schema.processlist where command!='Sleep' and user not in ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', 'unauthenticated', 'ping')"
            ;;
        all)
            sql="select id from information_schema.processlist where user not in ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', 'unauthenticated', 'ping')"
            ;;
        *)
            ;;
    esac
    /usr/local/bin/lg $port -Ne "$sql" | sed 's/^/kill /g;s/$/;/g' | /usr/local/bin/lg $port -f

}
function stop() {
    port=$1
    prepare $port
    # $ADM -h0 -P$port -u$user -p$password flush-tables
    query -e "set sql_log_bin = 0; flush tables" || return 1
    event 1251 "mysqld maintain stop"
    $ADM -h0 -P$port -u$user -p$password shutdown
    while true
    do
        num=$(ps aux | grep mysqld_safe | grep -c $port)
        if [[ $num -eq 0 ]]
        then
            echo "mysqld $port shutdown"
            break
        fi
        sleep .5
    done
}

function start() {
    port=$(grep -oP '\d+' <<< $1)
    if [[ -n $port ]]
    then
        cmd=$(grep "$port" /etc/rc.local)
        eval "$cmd"
        event 1252 "mysqld maintain start"
        sleep .5
        echo "mysqld $port start"
    else
        echo "port $1 not exists"
        exit 1
    fi
}

function restart() {
    port=$1
    stop $port
    start $port
}

function lg() {
    port=$1
    prepare $port
    echo "-h0 -P$port -u$user -p$password"
}


function tcp() {
    netstat -nat | awk '$6=="ESTABLISHED"&&$4~/:'$1'/{gsub(/:.+/,"",$5);print $5}' | sort -u
}

function dump() {
    port=$1
    prepare $port
    echo "mysqldump -h0 -P$port -u$user -p$password --single-transaction --default-character-set=utf8 --skip-add-locks --skip-lock-tables --apply-slave-statements --flush-privileges  --master-data=1"
}

function slave() {
    echo "change master to master_host='', master_port=, master_user='slave', master_password='', master_heartbeat_period=5;
change master to master_log_file='mysql-bin.000001', master_log_pos=0;"
}

function skip() {
    port=$1
    prepare $port
    bar=('-' '\\' '|' '/')
    i=0
    error=0
    eval $(awk '/=/{gsub(/ /,"");gsub(/>/,"");print}' /etc/snmp/yyms_agent_db_scripts/db_$port.conf) || exit 1
    while true
    do
        eval $(query -e "show slave status\G" | sed -n '/Last_SQL_Errno/{s/ //g;s/:/=/g;p}')
        tput  sc
        ((i++))
        case $Last_SQL_Errno in
            1032|1062|1452)
                query -e "stop slave;set global sql_slave_skip_counter = 1;start slave" 2>/dev/null
                error=$[error+1]
                            ;;
            *)
                            ;;
        esac
        printf --  "skiped $error errors ... .... ${bar[$[i%4]]}"
        tput rc
        sleep .2
    done
}

function grant() {
    # iptables -I INPUT -s $ip -p tcp -m tcp --dport $port -j ACCEPT
    # grant all privileges on *.* to 'db_myshard_rw'@'127.0.0.1' identified by 'hso,8H16Hb4.'
    port=$1
    user=$2
    password=$3
    ip=$4
    if [[ -z $ip ]]
    then
        echo 'adm grant $user $password $ip'
        exit 1
    fi
    if ! grep -qP "\s$ip.+$port\s+-j ACCEPT" /usr/local/virus/iptables/iptables.add
    then
        echo "iptables -I INPUT -s $ip -p tcp -m tcp --dport $port -j ACCEPT" >> /usr/local/virus/iptables/iptables.add
        iptables -I INPUT -s $ip -p tcp -m tcp --dport $port -j ACCEPT
    fi
    /usr/local/bin/lg $port -e "grant all privileges on *.* to '$user'@'$ip' identified by '$password'"
}


function pt() {
    port=$1
    prepare $port
    schema="$2"
    table="$3"
    ddl="$4"
    char=$($MySQL -A -h0 -P $port -u $user -p$password -Ne "show variables like 'character_set_server'" | awk '{print $2}')
    query -e "set global innodb_stats_on_metadata=0"
    echo "pt-online-schema-change --critical-load Threads_running=1500 --set-vars innodb_lock_wait_timeout=50 --check-interval=2 --charset=$char --drop-old-table --nocheck-replication-filters --execute  --alter '$ddl' h=127.0.0.1,P=$port,u=db_monitor,p='${password/,/\\,}',D=$schema,t=$table"
}

"$@"