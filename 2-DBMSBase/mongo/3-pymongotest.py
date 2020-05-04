#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/9 10:49
# @user: Administrator
# @fileName: 3-pymongotest.py
# @description: 用于连接mongoDB测试连接，执行管理命令
#
# command 支持的命令参考：
# https://docs.mongodb.com/manual/reference/command/
# 对于密码中出现 / 这个处理比较麻烦
# mongo 测试实例：
#

import os
import urllib
import commands
import pymongo


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
    getDbmsPassword = "/data/dbms/dba-tools/bin/dba-tools com.yy.dba.dbms.tools.DbmsPassword -d {}".format(
        mongoLogInfo["password"])
    status, output = commands.getstatusoutput(getDbmsPassword)
    if not status:
        mongoLogInfo["password"] = output
        return mongoLogInfo
    else:
        print "get Mongo user password failed"


def mongoConnectUri():
    # 通过urllib来处理可能出现的 / 等特殊字符
    username = urllib.quote_plus(login["username"])
    password = urllib.quote_plus(login["password"])
    port = int(login["port"])
    print username
    print password
    mongoUri = "mongodb://{}:{}@127.0.0.1:{}/default_db?authSource=admin".format(username, password, port)
    print mongoUri
    mongoClient = pymongo.MongoClient(mongoUri)
    mongoAdmin = mongoClient.admin
    print mongoAdmin.command("isMaster")["ismaster"]


def main():
    mongoConnectUri()


if __name__ == '__main__':
    login = getMongoUserPass(10002)
    print login
    main()
