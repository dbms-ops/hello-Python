# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/21 18:09
# user: Administrator
# description: 脚本通过5个线程用于测试salt的连通性，用于加快 salt 连通性验证
#
import Queue
import argparse
import commands
import os
import threading


def read_server_id(file_path, server_id_queue):
    absPath = os.path.abspath('.') + '/' + file_path
    if os.path.exists(absPath):
        with open(absPath, 'r') as file_handler:
            while True:
                # Remove trailing newlines
                serverId = file_handler.readline().strip('\n')
                if not serverId:
                    break
                server_id_queue.put(serverId)
    else:
        print "no such file {}".format(absPath)


def run_salt_test(i, server_id_queue):
    while True:
        server_id = server_id_queue.get()
        if server_id is None:
            break
        saltCommands = "/data1/Python-2.7.4/bin/salt 'minion_{}' test.ping ".format(server_id)
        status, output = commands.getstatusoutput(saltCommands)
        if not status:
            print "thread id: {} server_id: {} test successful".format(i, server_id[0:-1])
        else:
            print "thread_id: {} server_id: {} test failed".format(i, server_id[0:-1])


def thread_start(filename):
    q = Queue.Queue()
    read_end = threading.Thread(target=read_server_id, args=(filename, q))
    read_end.start()
    salt_test_1 = threading.Thread(target=run_salt_test, args=(1, q))
    salt_test_2 = threading.Thread(target=run_salt_test, args=(2, q))
    salt_test_3 = threading.Thread(target=run_salt_test, args=(3, q))
    salt_test_1.start()
    salt_test_2.start()
    salt_test_3.start()
    salt_test_1.join(timeout=1)
    salt_test_2.join(timeout=1)
    salt_test_3.join(timeout=1)
    read_end.join(timeout=1)
    exit(0)


def main():
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    parser = argparse.ArgumentParser(prog="salt-test", usage="test salt and run ping command",
                                     description='test salt command', epilog="version: 1.0")
    parser.add_argument('file', help='the file which content server_id information')
    args = parser.parse_args()
    filename = args.file
    thread_start(filename)


if __name__ == '__main__':
    main()
