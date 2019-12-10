#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#
# 字符串函数

print "你好"
string = "hello,world"

# isspace():用于判断是否是空白字符
name = 'hello, are tom'
i = 0
while i < len(name):
    if name[i].isspace():
        print i
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
print name[start:end]

















