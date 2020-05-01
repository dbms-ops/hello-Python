#!/data1/Python2.7/bin/python27
# -*-coding:utf-8-*-
# time: 2020-01-24 10:21
# user: linux
# description: 开始学习Python的第一个脚本

import os
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



print os.getcwd()
os.chdir("/tmp/")
print os.getcwd()




if __name__ == '__main__':
    pass


