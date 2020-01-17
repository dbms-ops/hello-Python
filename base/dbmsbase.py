# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/17 17:28
# user: Administrator
# description: 实现 dbms 操作的一些基本功能
#

import os


class Dbms():
    def __init__(self):
        pass

    def lgInfo(self, type, port):
        """
        Username and password information for finding applications that need to log in
        :param type: Type of database,Supports a database that requires a password to log in and a service profile
         exists
        :param port: Service working port
        :return: Returns a dictionary containing usernames and passwords;
        """
        login = {'user': '', 'password': ''}
        filepath = "".format(type, port)
        if os.path.exists(filepath):
            with open(filepath, 'r') as fread:
                while fread.readline():
                    line = fread.readline()
                    if line.startswith('user'):
                        login['user'] = line.split('=')[1][0:-1]
                    if line.startswith('password'):
                        login['password'] = line.split('=')[1][0:-1]
                        return login
        return None


def main():
    mysql = Dbms()
    result = mysql.lgInfo('db', 6302)
    print result['user']
    print result['password']


if __name__ == '__main__':
    main()
