#!/data1/Python2.7/bin/python27
# -*-coding:utf-8-*-
# time: 2020-01-24 10:21
# user: linux
# description: 字符串函数
#
#

from __future__ import print_function

print('你好')
print('112')
string = "hello,world"

# isspace():用于判断是否是空白字符
name = 'hello, are tom'
i = 0
while i < len(name):
    if name[i].isspace():
        print(i)
    i += 1

# 删除字符串结尾和开头的所有空格
#
name = "    dadasd,dad dasd aalwiqalk     "
index = 0
while index < len(name):
    if name[index].isspace():
        index += 1
    else:
        start = index
        break
index = len(name) - 1
while index > 0:
    if name[index].isspace():
        index -= 1
    else:
        end = index
        break
print(name[start:end])

# find：用于进行字符串查找
s = "Pycharm is a prefect IDE,You should buy for it"
print(s.find("should"))
print(s.rfind("should"))
