#!/data1/Python2.7/bin/python27
# -*-coding:utf-8-*-
# time: 2020-01-24 10:21
# user: linux
# description: 通过递归，深度遍历，广度遍历等方式实现递归查找所有的文件的目录
# 
import collections
import os


# 通过递归实现打印所有的文件和目录
def list_all(dpath, sp=" "):
    file_list = os.listdir(dpath)
    sp += " "
    for fileName in file_list:
        # 判断是否是文件或者是目录需要使用绝对路径
        if os.path.isdir(os.path.join(dpath, fileName)):
            print sp + "dir: {}".format(fileName)
            list_all(fileName, sp)
        else:
            print sp + fileName


# 使用栈结构实现listAll()
# 深度遍历原则
# 栈的先进后出是实现深度遍历的基础

def listalldeep(dpath):
    stack = []
    # 从栈里面取出数据，当栈为空时，结束循环
    stack.append(dpath)
    while len(stack) != 0:
        # 从栈里面取出数据
        dirPath = stack.pop()
        # 目录底下的所有文件
        filelist = os.listdir(dirPath)
        # 循环遍历文件或者是目录列表
        for fileName in filelist:
            fileabspath = os.path.join(dirPath, fileName)
            if os.path.isfile(fileabspath):
                print fileName
            else:
                print "dir: " + fileName
                stack.append(fileabspath)


# 队列实现广度遍历
# 队列的先进先出特性是实现广度遍历的基础

def getalldirpath(dpath):
    filequeue = collections.deque()
    # 将数据进队
    filequeue.append(dpath)

    while len(filequeue) != 0:
        # 数据出队列
        dirpath = filequeue.popleft()
        # 找出所有的文件
        fileall = os.listdir(dirpath)
        for file in fileall:
            fileabspath = os.path.join(dirpath, file)
            if os.path.isfile(fileabspath):
                print "文件：" + fileabspath
            else:
                filequeue.append(fileabspath)


if __name__ == '__main__':
    pass
