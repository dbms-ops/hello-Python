#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-18 18:13 
# user: linux
# description: pymysql 模块的使用
# 
import pymysql


def connect_db():
    db = pymysql.connect('183.36.110.112', '6311', 'westos', 'westos')
    cursor = db.cursor()
    cursor.execute('select version();')
    result = cursor.fetchone()[0]
    db.commit()
    print str(result).startswith('5.1')


def main():
    connect_db()


if __name__ == "__main__":
    main()
