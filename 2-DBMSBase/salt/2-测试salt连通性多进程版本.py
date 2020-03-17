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


def readServerId(file_path):
    absPath = os.path.abspath('.') + '/' + file_path
    if os.path.exists(absPath):
        with open(absPath, 'r') as file_handler:
            while True:
                # Remove trailing newlines
                serverId = file_handler.readline().strip('\n')
                if not serverId:
                    break
                yield serverId
    else:
        print "no such file {}".format(absPath)


def runSaltTest(i, server_id_queue, successful, failed):
    while True:
        try:
            server_id = server_id_queue.get(block=True, timeout=3)
        except Queue.Empty:
            break
        saltCommands = "/data1/Python-2.7.4/bin/salt 'minion_{}' test.ping ".format(server_id)
        status, output = commands.getstatusoutput(saltCommands)
        if not status:
            successful += 1
            print "thread id: {} server_id: {} test successful".format(i, server_id[0:-1])
        else:
            failed += 1
            print "thread_id: {} server_id: {} test failed".format(i, server_id[0:-1])
    print "summary: succeeded:{} failed:{}".format(successful, failed)


def threadStart(filename):
    q = Queue.Queue()
    for server_id in readServerId(filename):
        q.put(server_id, block=True, timeout=1)
    successful = 0
    failed = 0
    for I in range(3):
        threading.Thread(target=runSaltTest, args=(I, q, successful, failed))


def main():
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    parser = argparse.ArgumentParser(prog="salt-test", usage="test salt and run ping command",
                                     description='test salt command', epilog="version: 1.0")
    parser.add_argument('file', help='the file which content server_id information')
    args = parser.parse_args(['server_id'])
    filename = args.file
    threadStart(filename)


if __name__ == '__main__':
    main()
