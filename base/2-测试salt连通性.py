# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/20 18:10
# user: Administrator
# description: 脚本用于测试 salt 远程调用的连通性
#

import argparse
import commands
import os


# import sys

# reload(sys)
# sys.setdefaultencoding("utf-8")


def testSalt(filename):
    """
    This function is used to test the connectivity of salt. The passed filename should contain server_id and should be
    cut by newline characters.
    :param filename: Parameter represents a file name containing server_id
    :return:
    """
    absPath = os.path.abspath('.') + '/' + filename
    if os.path.exists(absPath):
        failed = 0
        successful = 0
        with open(absPath, 'r') as file_handler:
            while True:
                # Remove trailing newlines
                serverId = file_handler.readline().strip('\n')
                if not serverId:
                    break
                saltCommands = "/data1/Python-2.7.4/bin/salt 'minion_{}' test.ping ".format(serverId)
                status, output = commands.getstatusoutput(saltCommands)
                if not status:
                    print "server_id: {} test successful".format(serverId[0:-1])
                    successful += 1
                else:
                    print "server_id: {} test failed".format(serverId[0:-1])
                    failed += 1
            print "summary test ended: successful: {} and failed: {}".format(successful, failed)
    else:
        print "no such file {}".format(absPath)


def main():
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    parser = argparse.ArgumentParser(prog="salt-test", usage="test salt and run ping command",
                                     description='test salt command', epilog="version: 1.0")
    parser.add_argument('file', help='the file which content server_id information')
    args = parser.parse_args()
    filename = args.file
    print filename
    testSalt(filename)


if __name__ == '__main__':
    main()
