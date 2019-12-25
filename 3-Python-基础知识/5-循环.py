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

# 死循环：
#   表达式永远为真的循环
#

# while - else
# while 表达式1：
#   语句1
# else：
#   语句2


# for 循环：
#   for 变量 in 集合：
#       语句1
#
#   逻辑：
#       按照顺序去集合中的每个元素，赋值给变量
#       然后执行语句；

sum1 = 0
for I in range(1, 10, 1):
    sum1 += I
print sum1

# range(): 用于生成数列
#   range(10) 0--> 9
#   range(10,100,2) ---> 10-->100 步长为2；
#
# enumerate([1,2,3,4,5]):用于取出列表中元素的下标
#

for index, num in enumerate([1, 2, 3, 4, 5, 6]):
    print index, num

# break and continue
#  在循环内部，用于跳出最近一层循环
#  continue: 跳过当前循环的剩余语句，继续下一次循环
#
#


import turtle



if __name__ == '__main__':
    pass
