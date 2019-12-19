# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# 循环：while and for
# while 表达式：
#   语句1
# 语句2
# 如果表达式为真执行允许语句1，执行完成，计算表达式的值；
#   否则执行语句2
#
#

sum = 0
i = 1
while i < 100:
    sum += i
    i += 1
print sum

str1 = "A bully is always a coward"
index = 0
while index < len(str1):
    if str1[index] != ' ':
        print str1[index]
    index += 1

#


if __name__ == '__main__':
    pass
