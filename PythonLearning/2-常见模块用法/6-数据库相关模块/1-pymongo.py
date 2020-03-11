#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-07 21:44 
# user: lixun
# description: 脚本用于测试 pymongo 连接mongo的相关情况
# 
import urllib

import pymongo


# 对于副本集，需要直到所有的IP地址，和副本集名称，进行同步，可以自动连接从节点
def mongoClient(mongoIP, mongoPort, mongoUser, mongoPass):
    username = urllib.quote_plus(mongoUser)
    password = urllib.quote_plus(mongoPass)
    port = int(mongoPort)
    mongoUri = "mongodb://{}:{}@127.0.0.1:{}/default_db?authSource=admin".format(username, password, port)
    mongoConnections = pymongo.MongoClient(mongoUri)
    mongoAdmin = mongoConnections.admin
    print mongoAdmin.command("isMaster")["ismaster"]


def main():
    mongoClient('127.0.0.1', 10002, 'db_monitor', 'mongopass')

if __name__ == "__main__":
    main()
