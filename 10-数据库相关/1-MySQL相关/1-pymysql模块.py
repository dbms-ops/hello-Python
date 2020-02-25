#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-02-16 19:24
# user: linux
# description: 测试MySQL连接
#
#
# config = {
#           'host':'127.0.0.1',
#           'port':3306,
#           'user':'root',
#           'password':'zhyea.com',
#           'db':'employees',
#           'charset':'utf8mb4',
#           'cursorclass':pymysql.cursors.DictCursor,
#           ''
#           }
#
#
import pymysql

login = {'password': '6ZCdJ5zzh6', 'user': 'db_monitor'}


def query(sql):
    result = 1
    databaseQuery = pymysql.connect(host='127.0.0.1',
                                    port=6301,
                                    user=login['user'],
                                    password=login['password']
                                    )
    try:
        with databaseQuery.cursor() as databaseQueryCursor:
            databaseQueryCursor.execute(sql)
            result = databaseQueryCursor.fetchall()
    finally:
        databaseQuery.close()
        return result


def main():
    result = query(
        'SHOW GLOBAL STATUS WHERE Variable_name IN ("Com_select","Com_insert","Com_update","Com_delete","Uptime");')
    print result


if __name__ == "__main__":
    main()
