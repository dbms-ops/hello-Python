#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-07 21:44 
# user: lixun
# description: 脚本用于测试 pymongo 连接mongo的相关情况
#

import urllib
import pprint
import pymongo


# 对于副本集，需要直到所有的IP地址，和副本集名称，进行同步，可以自动连接从节点

class MongoDbms:

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    def _get_snmp(self):
        pass


class mongoTest:
    def __init__(self, ip, port, user, password):
        self._ip = ip
        self._port = port
        self._user = user
        self._password = password
        self._connection = self._mongoClient()

    def _mongoClient(self):
        username = urllib.quote_plus(self._user)
        password = urllib.quote_plus(self._password)
        port = int(self._port)
        mongoUri = "mongodb://{}:{}@{}:{}/default_db?authSource=admin".format(username, password, self._ip, port)
        mongoConnections = pymongo.MongoClient(mongoUri)
        return mongoConnections

    def list_database(self):
        return [database.encode('utf-8') for database in self._connection.list_database_names(session=None)]

    def mongoAdmin(self, database, command):
        db_connect = self._connection[database]
        return db_connect.command(command)

    def createIndex(self, database, collections=None, indexe=None):
        if collections and indexe:
            db_connect = self._connection[database]
            # db_connect[collections].create_index(indexes)
            return db_connect[collections].index_information(session=None)

    def adminCommand(self, command):
        # https://docs.mongodb.com/manual/reference/command/
        return self._connection.admin.command(command)

    def userCommand(self, database, command):
        pass

    def listCollections(self, database):
        return self._connection[database].list_collection_names(session=None)

    def createUser(self, user, password):
        pass



def main():
    mongo = mongoTest('14.17.108.123', 10005, 'tom', 'tom')
    print mongo.listCollections('haidaolaile')
    # mongo.createIndex(database='haidaolaile',collections='board',indexes=['{fromUid:-1},{background:true}'])


if __name__ == "__main__":
    main()
