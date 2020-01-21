# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/21 18:09
# user: Administrator
# description: 脚本通过5个线程用于测试salt的连通性，用于加快 salt 连通性验证
# 
import os
import threading


def read_server_id(file_path):
    serverIdList = []
    absPath = os.path.abspath('.') + '/' + file_path
    if os.path.exists(absPath):
        with open(absPath, 'r') as file_handler:
            while True:
                # Remove trailing newlines
                serverId = file_handler.readline().strip('\n')
                if not serverId:
                    break
                serverIdList.append(serverId)
    else:
        print "no such file {}".format(absPath)
    return serverIdList


def run_salt_test(server_id):
    pass


def run_thread_test_salt(server_id_list):
    for server_id in server_id_list:
        threading.Thread(target=)


def main():
    pass


if __name__ == '__main__':
    main()
