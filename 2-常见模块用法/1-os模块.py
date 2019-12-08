# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#

import os

print "获取当前脚本工作的目录路径: "
print os.getcwd()

print "修改当前目录为path"
os.chdir("/Users/lixun/PycharmProjects/LeartPython/")
print os.getcwd()

os.system("ls")


