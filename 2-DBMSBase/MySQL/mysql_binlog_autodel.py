#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/25 16:49
# @user: Administrator
# @fileName: mysql_binlog_autodel.py.py
# @description: 用于自动清理 binlog
# 
# !/data1/Python-2.7.4/bin/python
# coding=utf-8
# 跳过数据库错误
# 磁盘满binlog自动清理
from __future__ import division

import argparse
import commands
import glob
import json
import os
import random
import sys
import time

from mysql_base import dbconn, logger, ps_count, alarm, configuration


def check_binlog():
    try:
        disk_percent = 0
        if os.path.exists('/data') and os.path.ismount('/data'):
            cmd = "df  /data|tail -1 |awk '{print $(NF-1)}'"
            disk_percent = int(commands.getoutput(cmd).strip('%'))
        return disk_percent
    except Exception as error:
        msg = '{"code":"999","message":"%s"}' % (error)
        return 0


def binlog_purge(myconn, port, binlogcount=200, keepsize=20):
    # code>99的都告警
    try:
        sql = "show global variables like 'log_bin_basename';"
        sqlresult = myconn.myquery(sql)
        dirname = os.path.dirname(sqlresult[0]['Value'])
        msg = {"code": "100", "message": "message error"}
        if os.path.exists(dirname):
            cmd = "du -sk %s |awk '{print $1}'" % (dirname)
            filesize = int(commands.getoutput(cmd))
            ###binlog 满 keepsizeGB以上才发起清理
            if filesize > keepsize * 1024 * 1024:
                sql = "select count(1) as slavecount from PROCESSLIST where COMMAND='Binlog Dump' and STATE not like 'Master has sent all binlog to slave%';"
                for one in range(3):
                    sqlresult = myconn.myquery(sql)
                    if sqlresult[0]['slavecount'] > 0:
                        time.sleep(1)
                        continue
                    else:
                        sql = 'show master logs'
                        sqlresult = myconn.myquery(sql)
                        loglen = len(sqlresult)
                        ##确定清理日志的位置。一次清理一半日志。
                        midposition = loglen - binlogcount
                        if loglen > binlogcount:
                            midposition = int(loglen / 2)
                        elif loglen > (binlogcount / 2) and loglen < binlogcount:
                            midposition = loglen - binlogcount
                        else:
                            msg = '{"code":"101","message":"%s cannot purge binlog"}' % (port)
                            return msg
                        # 至少保留binlogcount个日志
                        if loglen - midposition > binlogcount and midposition > 0:
                            logname = sqlresult[midposition]['Log_name']
                            purgesql = "PURGE BINARY LOGS TO '%s'" % (logname)
                            ###执行语句
                            myconn.myquery(purgesql)
                            msg = '{"code":"102","message":"instance %s execute %s success allbinlog %s purged %s "}' % (
                                port, purgesql, loglen, midposition)
                        else:
                            msg = '{"code":"103","message":"%s ,binlog清理完不足%s,清理失败"}' % (port, binlogcount)
                        return msg
                    msg = '{"code":"104","message":"%s  slave not sync,cannot purge binlog"}' % (port)
                    return msg
            else:
                msg = '{"code":"105","message":"%s binlog size no more then %sGB cannot purge binlog"}' % (
                    port, keepsize)
                return msg
    except Exception, error:
        msg = '{"code":"999","binlog_purge error":"%s"}' % (error)
        return msg


def main_pro(fileport, keepbinlogcount, keepsize=30, keeppercent=90):
    myconfdir = '/etc/snmp/yyms_agent_db_scripts'
    if fileport == 0:
        mycnf = glob.glob('{}/db_*.conf'.format(myconfdir))
    else:
        portcnf = ('%s/db_%s.conf') % (myconfdir, fileport)
        mycnf = glob.glob(portcnf)
    # 对配置文件列表进行随机排序，保证不会每次调起都先清理某一个。
    random.shuffle(mycnf)
    for cnf in mycnf:
        try:
            ###获取数据库连接
            _mysqlinfo = configuration(cnf)
            user = _mysqlinfo['user']
            password = _mysqlinfo['password']
            port = _mysqlinfo['port']
            host = '127.0.0.1'
            # 加入配置文件的阈值,和输入阈值的拿最小值,且最小值有限制
            disk_keeppercent = _mysqlinfo.get('disk_keeppercent', 80)
            binlog_keepsize = _mysqlinfo.get('binlog_keepsize', 20)
            binlog_keepcount = _mysqlinfo.get('binlog_keepcount', 200)
            keeppercent = min(int(disk_keeppercent), keeppercent)
            keepsize = min(keepsize, int(binlog_keepsize))
            keepbinlogcount = min(int(binlog_keepcount), keepbinlogcount)
            if keeppercent < 40: keeppercent = 40
            if keepsize < 5: keepsize = 5
            if keepbinlogcount < 80: keepbinlogcount = 80
            lg.info((port, keeppercent, keepbinlogcount, keepsize))

            myconn = dbconn(host, port, user, password)
            if not myconn.succ:
                msg = '{"code":"999","message":"%s"}' % (port)
                continue
            disk_percent = check_binlog()
            if disk_percent > keeppercent:
                msg = '{"code":"100","message":"disk /data more then %s percent,%s begin execute binlog_purge"}' % (
                    keeppercent, port)
                lg.info(msg)
                msg = binlog_purge(myconn, port, keepbinlogcount, keepsize)
                lg.info(msg)
                msg2 = json.loads(msg)
                if int(msg2['code']) == 102:
                    alarm(45241, 145533, 0, port, 3, msg2['message'])
            else:
                msg = '{"code":"0","message":" space enough ,check ok"}'
                lg.info(msg)
                return msg
        except Exception as error:
            msg = '{"code":"999","message":"%s"}' % (error)
            lg.info(msg)
            return msg


if __name__ == "__main__":
    dbname = 'information_schema'
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    logfile = "/tmp/%s_logfile.log" % (filename.rstrip(".py"))
    parser = argparse.ArgumentParser(description='监控临时表使用情况')
    parser.add_argument('-p', '--port', type=int, required=True, help=" 本实例 port 所有实例 0")
    parser.add_argument('-kp', '--keeppercent', type=int, required=False, default=80, help="data盘数据到百分之多少触发清除")
    parser.add_argument('-ks', '--keepsize', type=int, required=False, default=20, help="清除binlog时,binlog目录必须大于多少GB")
    parser.add_argument('-kc', '--keepbinlogcount', type=int, required=False, default=200,
                        help="保留多少个binlog大于keepbinlogcount个")
    args = parser.parse_args()
    fileport = args.port
    keeppercent = args.keeppercent
    keepsize = args.keepsize
    keepbinlogcount = args.keepbinlogcount
    # logfile='/tmp/mysql_binlog_autodel_script_logfile.log'
    # logfile=None
    lg = logger('info', logfile)
    ps_count(3)
    main_pro(fileport, keepbinlogcount, keepsize, keeppercent)
