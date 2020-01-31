#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-24 10:21
# user: linux
# description:  默认在输入时是以换行结尾的，通过下面的函数来改变这种行为
# 这个代码在2.7或者mac上面是会出错的

endstr = 'EOF'
output = ''
for line in iter(input, endstr):
    output += line + '\n'

print str

