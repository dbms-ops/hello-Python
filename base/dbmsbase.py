# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/17 17:28
# user: Administrator
# description: 实现 dbms 操作的一些基本功能
#

import os
import socket
import commands
import re


class Dbms(object):

    def lg_user_passwd(self, db_type, port):
        """
        Username and password information for finding applications that need to log in
        :param type: Type of database,Supports a database that requires a password to log in and a service profile
         exists
        :param port: Service working port
        :return: Returns a dictionary containing usernames and passwords;
        """
        login = {'user': '', 'password': ''}
        filepath = "/etc/snmp/yyms_agent_{}_scripts/mongo_{}.conf".format(db_type, port)
        if os.path.exists(filepath):
            with open(filepath, 'r') as fread:
                while True:
                    line = fread.readline()
                    if line.startswith('user'):
                        login['user'] = line.split('=')[1][0:-1]
                    if line.startswith('password'):
                        login['password'] = line.split('=')[1][0:-1]
                        return login

    def port_is_listen(self, ip, port, timeout=10):
        """
        Function used to verify whether the port is listening.
        :param ip: IP address of the host.
        :param port: Port number of the host.
        :param timeout: Timeout for connection attempt. The default is 10 seconds.
        :return: Returns true if the port is listening, otherwise returns false.
        """
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(timeout)
        try:
            sk.connect((ip, port))
            sk.close()
            return True
        except:
            return False

    def write_file_append(self, file_path, content):
        pass

    def run_command(self, command):
        status, output = commands.getstatusoutput(command)
        return {'status': status, 'output': re.split(r'[\t\n\r\f\v]', output)}


def main():
    db = Dbms()
    print db.run_command('netstat -ntl | grep 3306')
    mysql_log_in = Dbms()
    mysql_log_in.lg_user_passwd('db', 6301)


if __name__ == '__main__':
    main()
