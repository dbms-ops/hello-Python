#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-02-16 19:24
# user: linux
# description: 用于管理MySQL的几个常见的工具
#
import commands
import json
import logging
import os
import sys
from time import sleep

import pymysql
import subprocess32


def baseLogging(level="debug", log_file=None):
    loggingLevel = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR, "warning": logging.WARNING,
                    "critical": logging.CRITICAL}
    loggingFormat = "%(asctime)s: %(levelname)s %(levelno)s %(message)s"
    dataFormat = "%Y-%m-%d  %H:%M:%S %p"
    if log_file is None:
        logging.StreamHandler(sys.stderr)
    else:
        logging.basicConfig(filename=log_file, filemode='a+', format=loggingFormat, level=loggingLevel[level],
                            datefmt=dataFormat)
    return logging


def logMsg(logMessage, level='info', to_json=False):
    logLevel = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR, "warning": logging.WARNING,
                "critical": logging.CRITICAL}
    if not to_json:
        lg.log(logLevel[level], logMessage)
    else:
        if isinstance(logMessage, dict) or isinstance(logMessage, list):
            lg.log(logLevel[level], json.dumps(logMessage, ensure_ascii=False, indent=2, separators=[",", ":"]))
        else:
            lg.log(logLevel[level], logMessage)


def getUserPass(databasePort):
    userPassword = {'user': '', 'password': ''}
    databasePath = '/etc/snmp/yyms_agent_db_scripts/db_{}.conf'.format(databasePort)
    logMsg('databasePath:{}'.format(databasePath), level='debug')
    if os.path.exists(databasePath):
        with open(databasePath, 'r') as fread:
            while True:
                line = fread.readline()
                if line.startswith('user'):
                    userPassword['user'] = line.split('=')[1][0:-1]
                if line.startswith('password'):
                    userPassword['password'] = line.split('=')[1][0:-1]
                    logMsg('return login:{} successful'.format(userPassword), level='debug')
                    return userPassword
    else:
        logMsg('no such file {}'.format(databasePath), level='error')


def databaseHostQuery(databasePort, querySql):
    queryResult = 1
    databaseQuery = pymysql.connect(host='127.0.0.1',
                                    port=int(databasePort),
                                    user=login['user'],
                                    password=login['password']
                                    )
    try:
        with databaseQuery.cursor() as databaseQueryCursor:
            queryCount = databaseQueryCursor.execute(querySql)
            logMsg('queryCount is {}'.format(queryCount), level='debug')
            queryResult = databaseQueryCursor.fetchall()
            if queryCount == 0:
                queryResult = "\n\n\n\n"
                logMsg('queryResult is 0, Reassign queryResult', level='debug')
    finally:
        databaseQuery.close()
        return queryResult


def databaseHostInsert(databasePort, insertStatement):
    insertResult = 1
    databaseInsert = pymysql.connect(host='127.0.0.1',
                                     port=databasePort,
                                     user=login['user'],
                                     password=login['password'],
                                     db='db',
                                     charset='utf8mb4'
                                     )
    logMsg('connect info: {}'.format(databaseInsert), level='debug')
    try:
        with databaseInsert.cursor() as databaseInsertCursor:
            logMsg('start run sql: {}'.format(insertStatement))
            insertResult = databaseInsertCursor.execute(insertStatement)
            logMsg("end run sql: {}".format(insertStatement))
            databaseInsert.commit()
            logMsg("run sql: {} end and commit".format(insertStatement))
    finally:
        databaseInsert.close()
        logMsg("return insertResult {} ".format(insertResult))
        return insertResult


def databaseStatus(databasePort):
    statusLogFile = "/tmp/mysql-{}.log".format(databasePort)
    logMsg('\n\n\nlog sql run result to: {}\n\n\n'.format(logfile), level='debug')
    sql = "SELECT  r.trx_id as locked_trx, r.trx_query as locked_sql, b.trx_id as block_id, b.trx_query " \
          "AS block_sql, b.trx_mysql_thread_id as block_thread, b.trx_started " \
          "AS block_start_time FROM(information_schema.innodb_lock_waits w " \
          "INNER JOIN information_schema.innodb_trx b " \
          "ON b.trx_id = w.blocking_trx_id) INNER JOIN information_schema.innodb_trx r " \
          "ON r.trx_id = w.requesting_trx_id ORDER BY b.trx_started DESC ;"
    logMsg('start run sql: {}'.format(sql), level='debug')
    databaseQueryUpshot = databaseHostQuery(databasePort, sql)
    with open(statusLogFile, 'w+') as fwrite:
        headInformation = 'MySQL {} deadlock log start\n'.format(databasePort).upper().center(114, '#')
        fwrite.writelines(headInformation)
        if databaseQueryUpshot is not None:
            fwrite.writelines(str(databaseQueryUpshot))
        else:
            fwrite.write("\n\n\n")
    sql = 'select @@performance_schema'
    performance = databaseHostQuery(databasePort, sql)
    if performance:
        sql = "SELECT  trx.trx_mysql_thread_id  thread_id, prl.host, prl.user, trx.trx_id, trx.trx_started, prl.time, " \
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
    databaseQueryUpshot = databaseHostQuery(databasePort, sql)
    with open(statusLogFile, 'w') as fwrite:
        headInformation = "\n\n\nMySQL {} deadlock log start \n\n\n".format(databasePort).upper().center(114, '#')
        fwrite.write(headInformation)
        fwrite.write(str(databaseQueryUpshot))

    sql = "SELECT  prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, prl.state, " \
          "trx.trx_state, trx.trx_query from information_schema.innodb_trx trx straight_join " \
          "information_schema.processlist prl on trx.trx_mysql_thread_id=prl.id order by trx.trx_started desc;"
    databaseQueryUpshot = databaseHostQuery(databasePort, sql)
    with open(statusLogFile, 'w+') as fwrite:
        headInformation = "\n\n\nMysql {} uncommitted \n\n\n".format(databasePort).upper().center(114, '#')
        fwrite.write(headInformation)
        fwrite.write(str(databaseQueryUpshot))

    sql = "SELECT prl.id, prl.user, prl.host, trx.trx_id, trx.trx_started, prl.time, prl.db, prl.command, prl.state, " \
          "trx.trx_state, trx.trx_query FROM information_schema.innodb_trx trx STRAIGHT_JOIN " \
          "information_schema.processlist prl ON trx.trx_mysql_thread_id=prl.id ORDER BY trx.trx_started DESC;"
    databaseQueryUpshot = databaseHostQuery(databasePort, sql)
    with open(statusLogFile, 'w+') as fwrite:
        headInformation = "\n\n\nmysqld {} transaction\n\n\n".format(databasePort).upper().center(114, '#')
        fwrite.write(headInformation)
        fwrite.write(str(databaseQueryUpshot))
    print "The databasePort {} status log in {}".format(databasePort, statusLogFile)


def qps(databasePort):
    print "Com_select                Com_insert                     Com_update              Com_delete".center(114, "#")
    for I in range(10):
        sql = 'SHOW GLOBAL STATUS WHERE Variable_name IN ("Com_select","Com_insert","Com_update",' \
              '"Com_delete","Uptime");'
        first_query = databaseHostQuery(databasePort, sql)
        first_query = dict(first_query)
        sleep(2)
        second_query = databaseHostQuery(databasePort, sql)
        second_query = dict(second_query)
        print "   {}                        {}                              {}                      {} ".format(
            (int(second_query['Com_select']) - int(first_query['Com_select'])) / 2.0,
            (int(second_query['Com_insert']) - int(first_query['Com_insert'])) / 2.0,
            (int(second_query['Com_update']) - int(first_query['Com_update'])) / 2.0,
            (int(second_query['Com_delete']) - int(first_query['Com_delete'])) / 2.0
        ).center(114, ' ')


def kill(databasePort, statusType):
    if statusType == 'sleep':
        sql = "SELECT id FROM information_schema.processlist WHERE command='Sleep' AND user NOT IN " \
              "('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', " \
              "'unauthenticated', 'ping');"
    elif statusType == 'idle':
        sql = "SELECT prl.id FROM information_schema.innodb_trx trx STRAIGHT_JOIN information_schema.processlist prl " \
              "ON trx.trx_mysql_thread_id=prl.id WHERE prl.command='Sleep' AND trx.trx_state='RUNNING' " \
              "ORDER BY trx.trx_started;"
    elif statusType == 'run':
        sql = "SELECT id FROM information_schema.processlist WHERE command!='Sleep' AND user " \
              "NOT IN ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', " \
              "'unauthenticated', 'ping');"
    elif statusType == "all":
        sql = "SELECT id FROM information_schema.processlist WHERE user " \
              "NOT IN ('event_scheduler','repl','root', 'db_monitor', 'slave', 'system user', 'unauthenticated user', " \
              "'unauthenticated', 'ping');"
    else:
        sql = 'select version()'
    databaseKill = pymysql.connect(host='127.0.0.1', port=databasePort, user=login['user'], password=login['password'])
    databaseKillCursor = databaseKill.cursor()
    databaseKillCursor.execute(sql)
    while True:
        databaseUpshot = databaseKillCursor.fetchone()
        if databaseUpshot is None:
            break
        sql = 'kill {}'.format(databaseUpshot)
        killConnections = databaseKill.cursor()
        killConnections.execute(sql)


def databaseAlive(databasePort):
    getUserPass(databasePort)
    aliveCommand = " /usr/local/mysql_{}/bin/mysqladmin -h'127.0.0.1' -u{} -p{} -P {} ping".format(databasePort,
                                                                                                   login['user'],
                                                                                                   login['password'],
                                                                                                   databasePort)
    logMsg('run status_command: {} '.format(aliveCommand), level='debug')
    aliveStatus, output = commands.getstatusoutput(aliveCommand)
    return not aliveStatus


def stop(databasePort):
    if databaseAlive(databasePort):
        stopMysqlCommand = "/usr/local/mysql_{}/bin/mysqladmin -h'127.0.0.1' -u{} -p{} -P {} shutdown " \
                           "".format(databasePort, login['user'], login['password'], databasePort)
        existsCommands = '/usr/local/mysql_{}/bin/mysqladmin'.format(databasePort)
        logMsg('run stop mysql-server: {} start'.format(stopMysqlCommand), level='debug')
        if os.path.exists(existsCommands):
            status, output = commands.getstatusoutput(stopMysqlCommand)
            if not status:
                print 'stop databasePort: {} successful!!'.format(databasePort)
                logMsg('stop databasePort: {} successful!!'.format(databasePort), level='debug')
            else:
                print "stop databasePort: {} failed".format(databasePort)
                logMsg('stop databasePort: {} failed!!'.format(databasePort), level='debug')
    else:
        print "mysql-server: {} is stopped".format(databasePort)
        logMsg('mysql-server: {} is stopped'.format(databasePort), level='debug')


def start(databasePort):
    logMsg('start {}'.format(databasePort), level='info')
    if not databaseAlive(databasePort):
        startMysql = ["/usr/bin/numactl", "--interleave=all", "/usr/local/mysql_{}/bin/mysqld_safe".format(
            databasePort), "--defaults-file=/data/mysql_{}/my.cnf".format(databasePort)]
        logMsg('run startMysql command:  {}'.format(startMysql), level='debug')
        try:
            subprocess32.run(startMysql, stdout=subprocess32.PIPE, stderr=subprocess32.PIPE,
                             timeout=10)
        except subprocess32.TimeoutExpired:
            logMsg('start command:{}  and get subprocess32.TimeoutExpired, but stop {} successful'.format(
                startMysql, databasePort
            ), level='debug')
            print "start {} successful".format(databasePort)
        except:
            logMsg('start {} failed'.format(databasePort), level='error')
            print "start {} failed".format(databasePort)

    else:
        print "mysql-server: {} is started".format(databasePort)
        logMsg("mysql-server {} is already started".format(databasePort), level='error')


def netstatTcp():
    tcpCommand = '''netstat -nat | awk '$6=="ESTABLISHED"&&$4~/:'$1'/{gsub(/:.+/,"",$5);print $5}' | sort -u'''
    tcpStatus, tcpOutput = commands.getstatusoutput(tcpCommand)
    if not tcpStatus:
        print tcpOutput
    else:
        print "run {} failed".format(tcpCommand)


def changeMaster():
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


def grantSlavePrivileges(slaveIP, slavePort, slaveUser='slave', slavePassword='slave'):
    # iptables -I INPUT -s $slaveIP -p tcp -m tcp --dport $slavePort -j ACCEPT
    # grant all privileges on *.* to 'db_myshard_rw'@'127.0.0.1' identified by 'hso,8H16Hb4.'
    existsIpAndPort = 'grep -qP "\s{}.+{}\s+-j ACCEPT" /usr/local/virus/iptables/iptables.add'.format(slaveIP,
                                                                                                      slavePort)
    existsOrNot, output = commands.getstatusoutput(existsIpAndPort)
    if existsOrNot:
        addIptablesTofile = 'echo "iptables -I INPUT -s {} -p tcp -m tcp --dport {} -j ACCEPT" >> ' \
                            '/usr/local/virus/iptables/iptables.add'.format(slaveIP, slavePort)
        commands.getstatusoutput(addIptablesTofile)
        addIptables = 'iptables -I INPUT -s {} -p tcp -m tcp --dport {} -j ACCEPT'.format(slaveIP, slavePort)
        commands.getstatusoutput(addIptables)
    else:
        logMsg("the IP: {} and port: {} has exists in iptables".format(slaveIP, slavePort), level='warning')
    grantPrivilegesSQL = "grant all privileges on *.* to '{}'@'{}' identified by {}".format(slaveIP,
                                                                                            slaveUser,
                                                                                            slavePassword)
    grantPrivilegesByLg = "/usr/local/bin/lg {} -e {}".format(slavePort, grantPrivilegesSQL)
    existsOrNot, output = commands.getstatusoutput(grantPrivilegesByLg)
    if not existsOrNot:
        print "grant to {}@{} successful".format(slaveUser, slavePassword)
        logMsg("grant privileges to {}@{} successful".format(slaveUser, slavePassword), level='debug')
    else:
        print "grant to {}@{} failed".format(slaveUser, slavePassword)
        logMsg("grant to {}@{} failed".format(slaveUser, slavePassword), level='error')


def main():
    print "start loh"
    logMsg('no such file ', level='error')


if __name__ == "__main__":
    # start logging
    dirname, filename = os.path.split(sys.argv[0])
    if not os.path.exists("/data/dba_logs/script"):
        os.popen2('mkdir -p /data/dba_logs/script')
    logfile = "/data/dba_logs/script/{}_logfile.log".format(filename.rstrip(".py"))
    lg = baseLogging(level='debug', log_file=logfile)
    logMsg(logMessage='this is a log file')
    choice_list_2 = ['tcp']
    choice_list_3 = ['start', 'stop', 'status', 'qps']
    choice_list_4 = ['kill']
    if len(sys.argv) == 3 and sys.argv[1] in choice_list_3:
        login = getUserPass(int(sys.argv[2]))
        choice = sys.argv[1]
        port = int(sys.argv[2])
        if choice == 'start':
            start(port)
        elif choice == 'stop':
            stop(port)
        elif choice == 'status':
            databaseStatus(port)
        elif choice == 'qps':
            qps(port)
    elif len(sys.argv) == 2 and sys.argv[1] in choice_list_2:
        choice = sys.argv[1]
        if choice == 'tcp':
            netstatTcp()
        else:
            pass
    elif len(sys.argv) == 4 and sys.argv[1] in choice_list_4:
        if sys.argv[1] == 'kill' and sys.argv[3] in ['sleep', 'idle', 'run', 'all']:
            login = getUserPass(int(sys.argv[2]))
            kill(int(sys.argv[2]), statusType=sys.argv[3])
        else:
            pass
    else:
        print """
            usage: 
                start   [port]: start port mysql-server
                stop    [port]: stop port mysql-server
                status  [port]: list the status mysql-server
                qps     [port]: print a list about mysqlqps
                tcp           : list tcp connections
                kill    [port] type in ['sleep','idle','run','all']:
        """
    main()
