# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/17 17:28
# user: Administrator
# description: 实现 dbms 操作的一些基本功能
#


import commands
import json
import logging
import os
import re
import socket


class Dbms(object):
    def getMongoUserPass(self, port):
        userPassword = {'username': '', 'password': ''}
        databasePath = "/etc/snmp/yyms_agent_mongo_scripts/mongo_{}.conf".format(port)
        if os.path.exists(databasePath):
            with open(databasePath, 'r') as fread:
                while True:
                    line = fread.readline()
                    if line.startswith('user'):
                        userPassword['username'] = line.split('user=')[1][0:-1]
                    if line.startswith('password'):
                        userPassword['password'] = line.split('password=')[1][0:-1]
                        break
        print userPassword
        getDbmsPassword = "/data/dbms/dba-tools/bin/dba-tools com.yy.dba.dbms.tools.DbmsPassword -d {}".format(
            userPassword["password"])
        status, output = commands.getstatusoutput(getDbmsPassword)
        if not status:
            userPassword["password"] = output
            return userPassword
        else:
            print "get Mongo user password failed"

    def getMySQLUserPass(self, port):
        """
        Username and password information for finding applications that need to log in
        :param type: Type of database,Supports a database that requires a password to log in and a service profile
         exists
        :param port: Service working port
        :return: Returns a dictionary containing usernames and passwords;
        """
        login = {'user': '', 'password': ''}
        filepath = "/etc/snmp/yyms_agent_db_scripts/db_{}.conf".format(port)
        if os.path.exists(filepath):
            with open(filepath, 'r') as fread:
                while True:
                    line = fread.readline()
                    if line.startswith('user'):
                        login['user'] = line.split('=')[1][0:-1]
                    if line.startswith('password'):
                        login['password'] = line.split('=')[1][0:-1]
                        return login

    def portIsListen(self, ip, port, timeout=10):
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

    def runCommand(self, command):
        status, output = commands.getstatusoutput(command)
        return {'status': status, 'output': re.split(r'[\t\n\r\f\v]', output)}

    def baseLogging(self, level="debug", log_file=None):
        loggingLevel = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR,
                        "warning": logging.WARNING,
                        "critical": logging.CRITICAL}
        loggingFormat = "%(asctime)s: %(levelname)s %(levelno)s %(message)s"
        dataFormat = "%Y-%m-%d  %H:%M:%S %p"
        if log_file is None:
            logging.StreamHandler(sys.stderr)
        else:
            logging.basicConfig(filename=log_file, filemode='a+', format=loggingFormat, level=loggingLevel[level],
                                datefmt=dataFormat)
        return logging

    def logMsg(self, logMessage, level='info', to_json=False):
        logLevel = {"debug": logging.DEBUG, "info": logging.INFO, "error": logging.ERROR, "warning": logging.WARNING,
                    "critical": logging.CRITICAL}
        if not to_json:
            lg.log(logLevel[level], logMessage)
        else:
            if isinstance(logMessage, dict) or isinstance(logMessage, list):
                lg.log(logLevel[level], json.dumps(logMessage, ensure_ascii=False, indent=2, separators=[",", ":"]))
            else:
                lg.log(logLevel[level], logMessage)



def main():
    db = Dbms()
    print db.runCommand('netstat -ntl | grep 3306')
    mysql_log_in = Dbms()
    mysql_log_in.getMySQLUserPass('db', 6301)


if __name__ == '__main__':
    main()
