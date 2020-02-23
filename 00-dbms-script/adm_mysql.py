#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-02-16 19:24
# user: linux
# description: 用于管理MySQL的几个常见的工具
#
import os
from time import sleep
import pymysql
import commands
import subprocess32
import json
import logging
import sys


def base_log(level="debug", log_file=None):
    log_level = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR,
                 "warning": logging.WARNING, "critical": logging.CRITICAL}
    log_format = "%(asctime)s: %(levelname)s %(levelno)s %(message)s"
    DATE_FORMAT = "%Y-%m-%d  %H:%M:%S %p"
    if log_file is None:
        logging.StreamHandler(sys.stderr)
    else:
        logging.basicConfig(filename=log_file, filemode='a', format=log_format, level=log_level[level],
                            datefmt=DATE_FORMAT)
    return logging


def base_lg(msg, level='info', to_json=False):
    log_level = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR,
                 "warning": logging.WARNING, "critical": logging.CRITICAL}
    if not to_json:
        lg.log(log_level[level], msg)
    else:
        if isinstance(msg, dict) or isinstance(msg, list):
            lg.log(log_level[level], json.dumps(msg, ensure_ascii=False, indent=2, separators=[",", ":"]))
        else:
            lg.log(log_level[level], msg)


def base_prepare(port):
    login = {'user': '', 'password': ''}
    db_path = '/etc/snmp/yyms_agent_db_scripts/db_{}.conf'.format(port)
    base_lg('db_path:{}'.format(db_path), level='debug')
    if os.path.exists(db_path):
        with open(db_path, 'r') as fread:
            while True:
                line = fread.readline()
                if line.startswith('user'):
                    login['user'] = line.split('=')[1][0:-1]
                if line.startswith('password'):
                    login['password'] = line.split('=')[1][0:-1]
                    base_lg('return login:{} successful'.format(login), level='debug')
                    return login
    else:
        base_lg('no such file {}'.format(db_path), level='error')


def query(port, statement):
    global result
    db_query = pymysql.connect(host='127.0.0.1',
                               port=port,
                               user=login['user'],
                               password=login['password'],
                               db='db',
                               charset='utf8mb4',
                               )
    base_lg("connect info: {}".format(db_query), level='debug')
    try:
        with db_query.cursor() as db_query_cursor:
            sql = statement
            base_lg('run sql: {}'.format(sql), level='debug')
            result = db_query_cursor.execute(sql)
            base_lg('log result: {} '.format(result), level='debug')
    finally:
        db_query.close()
        return result


def insert(port, statement):
    global result
    db_insert = pymysql.connect(host='127.0.0.1',
                                port=port,
                                user=login['user'],
                                password=login['password'],
                                db='db',
                                charset='utf8mb4'
                                )
    base_lg('connect info: {}'.format(db_insert), level='debug')
    try:
        with db_insert.cursor() as db_query_cursor:
            sql = statement
            base_lg('start run sql: {}'.format(sql))
            db_query_cursor.execute(sql)
            base_lg("end run sql: {}".format(sql))
            db_insert.commit()
    finally:
        db_insert.close()
        return result


def status(port):
    log_file = "/tmp/mysql-{}.log".format(port)
    base_lg('log sql run result to: {}'.format(logfile), level='debug')
    sql = "SELECT  r.trx_id as locked_trx, r.trx_query as locked_sql, b.trx_id as block_id, b.trx_query as block_sql, " \
          "b.trx_mysql_thread_id as block_thread, b.trx_started as block_start_time " \
          "FROM(information_schema.innodb_lock_waits w INNER JOIN information_schema.innodb_trx b " \
          "ON b.trx_id = w.blocking_trx_id) INNER JOIN information_schema.innodb_trx r " \
          "ON r.trx_id = w.requesting_trx_id ORDER BY b.trx_started DESC ;"
    base_lg('start run sql: {}'.format(sql))
    upshot = query(port, sql)
    with open(log_file, 'w+') as fwrite:
        start_log = 'MySQL {} deadlock log start\n'.format(port).upper().center(114, '#')
        fwrite.write(start_log)
        fwrite.write(upshot)

    sql = 'select @@performance_schema'
    performance = query(port, sql)
    if performance:
        sql = "SELECT trx.trx_mysql_thread_id thread_id, prl.host, prl.user, trx.trx_id, trx.trx_started, prl.time, " \
              "prl.db current_db, trx.trx_query current_sql, trx.trx_state, thd.processlist_command command, " \
              "last.current_schema last_db, last.sql_text last_sql FROM information_schema.innodb_trx trx " \
              "STRAIGHT_JOIN performance_schema.threads thd ON trx.trx_mysql_thread_id=thd.processlist_id " \
              "STRAIGHT_JOIN performance_schema.events_statements_current last ON thd.thread_id = last.thread_id " \
              "STRAIGHT_JOIN information_schema.processlist prl ON trx.trx_mysql_thread_id = prl.id " \
              "WHERE trx_state='running' AND command='sleep' ORDER BY trx.trx_started;"
    else:
        sql = "select  prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, " \
              "prl.state, trx.trx_state, trx.trx_query from information_schema.innodb_trx trx straight_join " \
              "information_schema.processlist prl on trx.trx_mysql_thread_id=prl.id where prl.command='Sleep' " \
              "and trx.trx_state='RUNNING' order by trx.trx_started;"
    upshot = query(port, sql)
    with open(log_file, 'w') as fwrite:
        start_log = "MySQL {} deadlock log start \n".format(port).upper().center(114, '#')
        fwrite.write(start_log)
        fwrite.write(upshot)

    sql = "SELECT  prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, prl.state, " \
          "trx.trx_state, trx.trx_query from information_schema.innodb_trx trx straight_join " \
          "information_schema.processlist prl on trx.trx_mysql_thread_id=prl.id order by trx.trx_started desc;"
    upshot = query(port, sql)
    with open(log_file, 'w+') as fwrite:
        start_log = "Mysql {} uncommitted \n".format(port).upper().center(114, '#')
        fwrite.write(start_log)
        fwrite.write(upshot)

    sql = "SELECT prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, prl.state, " \
          "trx.trx_state, trx.trx_query FROM information_schema.innodb_trx trx STRAIGHT_JOIN " \
          "information_schema.processlist prl ON trx.trx_mysql_thread_id=prl.id ORDER BY trx.trx_started DESC;"
    upshot = query(port, sql)
    with open(log_file, 'w+') as fwrite:
        start_log = "mysqld {} transaction".format(port).upper().center(114, '#')
        fwrite.write(start_log)
        fwrite.write(upshot)
    sql = "show engine innodb status\G"
    upshot = query(port, sql)
    with open(log_file, 'w+') as fwrite:
        start_log = "{}: Engine innodb status".format(port).upper().center(114, '#')
        fwrite.write(start_log)
        fwrite.write(upshot)
    print "The port {} status log in {}".format(port, log_file)


def qps(port):
    print "Com_select                Com_insert                     Com_update              Com_delete".center(114, "#")
    for I in range(10):
        sql = 'SHOW GLOBAL STATUS WHERE Variable_name IN ("Com_select","Com_insert","Com_update","Com_delete","Uptime");'
        first_query = query(port, sql)
        first_query = dict(first_query)
        sleep(2)
        second_query = query(port, sql)
        second_query = dict(second_query)
        print "   {}                        {}                              {}                      {} ".format(
            (int(second_query['Com_select']) - int(first_query['Com_select'])) / 2.0,
            (int(second_query['Com_insert']) - int(first_query['Com_insert'])) / 2.0,
            (int(second_query['Com_update']) - int(first_query['Com_update'])) / 2.0,
            (int(second_query['Com_delete']) - int(first_query['Com_delete'])) / 2.0
        ).center(114, ' ')


def kill(port, type):
    if type == 'sleep':
        sql = "SELECT id FROM information_schema.processlist WHERE command='Sleep' AND user NOT IN " \
              "('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', " \
              "'unauthenticated', 'ping');"
    elif type == 'idle':
        sql = "SELECT prl.id FROM information_schema.innodb_trx trx STRAIGHT_JOIN information_schema.processlist prl " \
              "ON trx.trx_mysql_thread_id=prl.id WHERE prl.command='Sleep' AND trx.trx_state='RUNNING' " \
              "ORDER BY trx.trx_started;"
    elif type == 'run':
        sql = "SELECT id FROM information_schema.processlist WHERE command!='Sleep' AND user " \
              "NOT IN ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', " \
              "'unauthenticated', 'ping');"
    elif type == "all":
        sql = "SELECT id FROM information_schema.processlist WHERE user " \
              "NOT IN ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', " \
              "'unauthenticated', 'ping');"

    else:
        sql = 'select version()'

    login = base_prepare(port)
    db = pymysql.connect('127.0.0.1', port, login['user'], login['password'])
    cursor = db.cursor()
    cursor.execute(sql)
    while True:
        upshot = cursor.fetchone()
        if upshot is None:
            break
        sql = 'kill {}'.format(upshot)
        kill_mysql = db.cursor()
        kill_mysql.execute(sql)


def is_alive(port):
    base_prepare(port)
    status_command = " /usr/local/mysql_{}/bin/mysqladmin -h'127.0.0.1' -u{} -p{} -P {} ping".format(port,
                                                                                                     login['user'],
                                                                                                     login['password'],
                                                                                                     port)
    base_lg('run status_command: {} '.format(status_command), level='debug')
    alive, output = commands.getstatusoutput(status_command)
    return not alive


def stop(port):
    if is_alive(port):
        stop_command = "/usr/local/mysql_{}/bin/mysqladmin -h'127.0.0.1' -u{} -p{} shutdown ".format(port,
                                                                                                     login['user'],
                                                                                                     login['password'])
        statement = '/usr/local/mysql_{}/bin/mysqladmin'.format(port)
        base_lg('run stop_command: {}'.format(stop_command), level='debug')
        if os.path.exists(statement):
            status, output = commands.getstatusoutput(stop_command)
            if not status:
                print 'stop port: {} successful!!'.format(port)
                base_lg('stop port: {} successful!!'.format(port), level='debug')
            else:
                print "stop port: {} failed".format(port)
                base_lg('stop port: {} failed!!'.format(port), level='debug')
    else:
        print "mysqld: {} is stopped".format(port)
        base_lg('mysqld: {} is stopped'.format(port), level='debug')


def start(port):
    if not is_alive(port):
        start_command = ["/usr/bin/numactl", "--interleave=all", "/usr/local/mysql_{}/bin/mysqld_safe".format(port),
                         "--defaults-file=/data/mysql_{}/my.cnf".format(port)]
        base_lg('run command: {} {}'.format("start_command", start_command), level='debug')
        try:
            subprocess32.run(start_command, stdout=subprocess32.PIPE, stderr=subprocess32.PIPE,
                             timeout=20)
        except subprocess32.TimeoutExpired:
            base_lg('stop command and get subprocess32.TimeoutExpired', level='debug')
            print "start {} successful".format(port)
            base_lg('start {} successful'.format(port))
        except:
            base_lg('start {} failed'.format(port))
            print "start {} failed".format(port)

    else:
        print "mysqld: {} is started".format(port)


def tcp():
    tcp_cmd = '''netstat -nat | awk '$6=="ESTABLISHED"&&$4~/:'$1'/{gsub(/:.+/,"",$5);print $5}' | sort -u'''
    upshot, output = commands.getstatusoutput(tcp_cmd)
    if not upshot:
        print output
    else:
        print "run {} failed".format(tcp_cmd)


def slave():
    print ''' change master to master_host='', 
    master_port=, 
    master_user='slave', 
    master_password='', 
    master_heartbeat_period=5,
    change master to master_log_file='mysql-bin.000001', 
    master_log_pos=0;'''


def skip_slave():
    print '''
    stop slave;
    set global sql_slave_skip_counter = 1;
    start slave;
    '''


def grant_slave(ip, port, user='slave', password='slave'):
    # iptables -I INPUT -s $ip -p tcp -m tcp --dport $port -j ACCEPT
    # grant all privileges on *.* to 'db_myshard_rw'@'127.0.0.1' identified by 'hso,8H16Hb4.'
    grep_commands = 'grep -qP "\s{}.+{}\s+-j ACCEPT" /usr/local/virus/iptables/iptables.add'.format(ip, port)
    return_value, output = commands.getstatusoutput(grep_commands)
    if return_value:
        iptables_add = 'echo "iptables -I INPUT -s {} -p tcp -m tcp --dport {} -j ACCEPT" >> ' \
                       '/usr/local/virus/iptables/iptables.add'.format(ip, port)
        commands.getstatusoutput(iptables_add)
        iptables_add = 'iptables -I INPUT -s {} -p tcp -m tcp --dport {} -j ACCEPT'.format(ip, port)
        commands.getstatusoutput(iptables_add)
    else:
        pass
    sql = "grant all privileges on *.* to '{}'@'{}' identified by {}".format(ip, user, password)
    grant_command = "/usr/local/bin/lg {} -e {}".format(port, sql)
    return_value, output = commands.getstatusoutput(grant_command)
    if not return_value:
        print "grant to {}@{} successful".format(user, password)
    else:
        print "grant to {}@{} failed".format(user, password)


def main():
    print "start loh"
    base_lg('no such file ', level='error')


if __name__ == "__main__":
    # start logging
    dirname, filename = os.path.split(sys.argv[0])
    if not os.path.exists("/data/dba_logs/script"):
        os.popen2('mkdir -p /data/dba_logs/script')
    logfile = "/data/dba_logs/script/{}_logfile.log".format(filename.rstrip(".py"))
    lg = base_log(level='info', log_file=logfile)
    base_lg(msg='this is a log file')
    login = base_prepare(6301)
    main()
