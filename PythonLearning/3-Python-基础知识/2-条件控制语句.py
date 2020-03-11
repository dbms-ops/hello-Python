# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/16 16:57
# user: Administrator
# description: 常见的条件控制语句：主要是单分支与多分支 if 语句
#

#
# 条件控制语句
# 条件控制语句一共包含三个：
# 1、
#   if 表达式：
#       语句1
#   语句2
#   如果表达式为真，执行语句1
#   否则执行语句2
#
# 2、
# 多分支if语句
#   if 表达式：
#         语句1
#   else:
#         语句2
#
#   如果表达式为真，执行表达式里面的语句
#   如果表达式为假，跳过if循环，执行后面的语句
# 为假：
#   0 0.0 '' None False
# 为真：
#   其余为真

# 通过下面的方式可以用于判断一个表达式真还是假


def True_or_Fales():
    if 0:
        print "True"
    else:
        print "False"

    if 0.0:
        print "true"
    else:
        print "False"

    if None:
        print "True"
    else:
        print "False"


# 判断传递的参数为真还是为假

def true_or_false(argu):
    """

    :param argu: Receive a parameter to determine true and false
    :return:
    """
    if argu:
        print "true"
    else:
        print "fasle"
    return True


# 3、条件控制语句
# if 表达式1：
#     语句1
# elif 表达式2：
#     语句2
# elif 表达式3：
#     语句3
# else:
#     语句4
# 语句
# 对于分支IF语句只会选择其中的一个分支执行，知道表达式为真则停止
#
def Multi_if():
    age = int(input("please input your age:"))

    if age < 0:
        print "no one"
    elif age <= 3:
        print "a baby"
    elif age <= 6:
        print "a children"
    elif age <= 18:
        print "youth"
    elif age <= 65:
        print "Adults"
    elif age <= 100:
        print "best"
    else:
        print "no person"


def main():
    Multi_if()
    True_or_Fales()


if __name__ == '__main__':
    main()
