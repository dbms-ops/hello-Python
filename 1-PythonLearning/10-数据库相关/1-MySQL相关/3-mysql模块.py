#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/17 11:51
# @user: Administrator
# @fileName: 3-mysql模块.py
# @description: mysql 模块是 oracle 提供的python 连接 MySQL的模块,用于实现基本的MySQL的管理功能
# 
import mysql.connector


def connectMysql():
    mysqlConnect = mysql.connector.connect(host="127.0.0.1", db='suc')
    mysqlConnect.get_server_info()


def main():
    pass


if __name__ == '__main__':
    main()
