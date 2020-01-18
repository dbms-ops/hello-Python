#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-18 18:13 
# user: linux
# description: pymysql 模块的使用
# 
import pymysql


def insert_data():
    db = pymysql.connect(('IP', 'port', 'user', 'password'))
    cursor = db.cursor()
    cursor.execute('select version();')


def main():
    pass


if __name__ == "__main__":
    main()
