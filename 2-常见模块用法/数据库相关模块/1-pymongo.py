#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-07 21:44 
# user: lixun
# description: 脚本用于测试 pymongo 连接mongo的相关情况
# 
from pymongo import MongoClient
from pymongo import ismaster
import pymongo
import pymongo.server_type
from pymongo import mongo_replica_set_client


# 对于副本集，需要直到所有的IP地址，和副本集名称，进行同步，可以自动连接从节点
def pymongoClient(mongoIP, mongoPort, mongoUser, mongoPass):
    mongoClient = MongoClient("mongodb://{}:{}@{}:{}/admin".format(mongoUser, mongoPass, mongoIP, mongoPort))
    mongoCollection = mongoClient.get_database("admin")
    mongoCollection.command()
    conn = mongo_replica_set_client()


def main():
    pass


if __name__ == "__main__":
    main()
