# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020-1-16 16:57
# user: Administrator
# description: 循环表达式 While 和 for
#

# 循环：while and for
# while 表达式：
#   语句1
# 语句2
# 如果表达式为真执行允许语句1，执行完成，计算表达式的值；
#   否则执行语句2
#
#


def while_sum_help():
    """
    add i from 1 to 99
    :return: return the sum from 1 to 99
    """
    result = 0
    i = 1
    while i < 100:
        result += i
        i += 1
    print result


def while_string_help():
    """
    print the string from zero to len(string) user index
    :return: no value
    """
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


def for_sum_help():
    """
    Calculate the sum of 1 to 10
    :return: print the sum of 1 to 10
    """
    sum1 = 0
    for I in range(1, 10, 1):
        sum1 += I
    print sum1


# break and continue
#  在循环内部，用于跳出最近一层循环
#  continue: 跳过当前循环的剩余语句，继续下一次循环
#
#


def main():
    while_sum_help()


if __name__ == '__main__':
    main()
