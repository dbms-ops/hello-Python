#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-18 18:13 
# user: linux
# description: pymysql 模块的使用
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


def connect_db():
    db = pymysql.connect(host='127.0.0.1', port='6301', user='db_monitor', password='6ZCdJ5zzh6')
    cursor = db.cursor()
    cursor.execute('select version();')
    result = cursor.fetchone()[0]
    db.commit()
    print result


def query():
    global db_connect
    try:
        db_connect = pymysql.connect(host='127.0.0.1',
                                     user='',
                                     password='',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with db_connect.cursor() as cursor:
            sql = 'select version()'
            cursor.execute(sql)
            db_connect.commit()
    finally:
        db_connect.close()



def main():
    connect_db()


if __name__ == "__main__":
    main()
