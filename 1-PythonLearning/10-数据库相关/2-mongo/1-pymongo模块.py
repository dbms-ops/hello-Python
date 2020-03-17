#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/9 10:49
# @user: Administrator
# @fileName: 1-pymongo 模块
# @description: 用于测试 pymongo的相关功能
#
# command 支持的命令参考：
# https://docs.mongodb.com/manual/reference/command/
# 对于密码中出现 / 这个处理比较麻烦
# mongo 测试实例：
#

import commands
import logging
import os
import sys
import urllib

import pymongo


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


def getMongoUserPass(port):
    mongoLogInfo = {'username': '', 'password': '', "port": port}
    databasePath = "/etc/snmp/yyms_agent_mongo_scripts/mongo_{}.conf".format(port)
    if os.path.exists(databasePath):
        with open(databasePath, 'r') as fread:
            while True:
                line = fread.readline()
                if line.startswith('user'):
                    mongoLogInfo['username'] = line.split('user=')[1][0:-1]
                if line.startswith('password'):
                    mongoLogInfo['password'] = line.split('password=')[1][0:-1]
                    break
    print mongoLogInfo
    logMsg("mongo user password port " + str(mongoLogInfo))
    logMsg("run com.yy.dba.dbms.tools.DbmsPassword get password, waiting 30s .......")
    getDbmsPassword = "/data/dbms/dba-tools/bin/dba-tools com.yy.dba.dbms.tools.DbmsPassword -d {}".format(
        mongoLogInfo["password"])
    status, output = commands.getstatusoutput(getDbmsPassword)
    if not status:
        mongoLogInfo["password"] = output
        logMsg("get mongo password successful" + str(mongoLogInfo))
        return mongoLogInfo
    else:
        logMsg("get mongo password failed script exit code: 10 .....", level='error')
        sys.exit(10)


def mongoConnectUri():
    # 通过urllib来处理可能出现的 / 等特殊字符
    username = urllib.quote_plus(login["username"])
    password = urllib.quote_plus(login["password"])
    port = int(login["port"])
    mongoUri = "mongodb://{}:{}@127.0.0.1:{}/default_db?authSource=admin".format(username, password, port)
    logMsg("connect mongo url: " + str(mongoUri))
    mongoClient = pymongo.MongoClient(mongoUri)
    mongoAdmin = mongoClient.admin
    logMsg("run mongo command: isMaster")
    print mongoAdmin.command("isMaster")["ismaster"]
    print mongoAdmin.command("ping")


def main():
    mongoConnectUri()


if __name__ == '__main__':
    # 日志函数初始化
    dirname, filename = os.path.split(sys.argv[0])
    if not os.path.exists("/data/dba_logs/script"):
        os.popen2('mkdir -p /data/dba_logs/script')
    logfile = "/data/dba_logs/script/{}_logfile.log".format(filename.rstrip(".py"))
    lg = baseLogging(level='debug', log_file=logfile)
    # 初始化函数，获取mongo用户名、密码；
    login = getMongoUserPass(10002)
    main()
