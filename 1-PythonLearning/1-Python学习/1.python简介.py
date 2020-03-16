#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-24 10:21
# user: linux
# description: 开始学习Python的第一个脚本

import platform

print "start learn python"

# declare a variable

i = 10
print i + 100
print type(i)

name = "hello"
print name, "the type is", type(name)

print platform.uname()[1]
print platform.machine()
print "你好"
print "hello"

import os

print os.getcwd()
os.chdir("D:\Python")
print os.getcwd()




if __name__ == '__main__':
    pass


