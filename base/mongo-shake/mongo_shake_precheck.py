#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-07 20:49 
# user: lixun
# description: 检查mongoDB的实例状态，用于安装mongo-shake工具
# 
import json, logging, os, sys, glob
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


def getUserPass(databasePort):
    userPassword = {'user': '', 'password': ''}
    databasePath = '/etc/snmp/yyms_agent_mongo_scripts/mongo_{}.conf'.format(databasePort)
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


def getMongoShakePort():
    logMsg("start allocate mongo shake port")
    if os.path.exists("/data/mongo-shake"):
        os.mkdir("/data/mongo-shake", mode=644)
    mongoShakeFile = glob.glob1("/data/mongo-shake", pattern="mongo-shake-\d{5}")
    mongoPort = len(mongoShakeFile) + 3320
    logMsg("allocate mongo shake port {} finished".format(mongoPort))
    return mongoPort


def checkSourceMongo(sourceIP, sourcePort):
    logMsg("start to check instance {}:{} status".format(sourceIP, sourcePort))


def main():
    pass


if __name__ == "__main__":
    # 日志函数初始化
    dirname, filename = os.path.split(sys.argv[0])
    if not os.path.exists("/data/dba_logs/script"):
        os.popen2('mkdir -p /data/dba_logs/script')
    logfile = "/data/dba_logs/script/{}_logfile.log".format(filename.rstrip(".py"))
    lg = baseLogging(level='debug', log_file=logfile)
    main()
