# !/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: tuple 的常见操作
#


# 数据结构-元组
#    元组：元组和列表类似，元祖内部的元素不可变；
#

def createTupleHelp():
    # 定义元素
    number = (1, 2, 3, 4, 5, 6, [1, 2, 3, 4])
    print type(number), number

    # 获取元组元素
    print number[0], number[1], number[2], number[-3]


def modifyTupleHelp():
    # 元组里面的元素是不允许进行修改的
    number = (1, 2, 3, 4, 5, 6, [1, 2, 3, 4])
    number[6][1] = "name"
    print number


def delTupleHelp():
    # 清空并且删除元组
    number = (1, 2, 3, 4, 5, 6, [1, 2, 3, 4])
    del number


# 元组的操作
# 元组相加

def tupleDdditionHelp():
    num = (1, 2, 3, 4, 5)
    name = ('alice', 'tom', 'jerry')
    print num + name


def repeatTupleHelp():
    # 元组重复
    num = (1, 2, 3, 4, 5)
    print num * 3


def inTupleHelp():
    # 元组包含
    num = (1, 2, 3, 4, 5)
    print 11 in num


def interceptHelp():
    # 元组截取
    num = (1, 2, 3, 4, 5, 6, 7, 8, 9) * 3
    print num
    print num[0:-1]
    print num[4:-4]


def twoDimensionalTupleHelp():
    # 二维元组
    num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print num


def lenHelp():
    # 元组的方法
    # 元组中元素的个数
    num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    len(num)


def maxHelp():
    # 元组中的最大值
    num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print max(num)


def minHelp():
    # 元组中的最小值
    num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print min(num)


def listToTupleHelp():
    # 列表转换元组
    num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    num = tuple(list(num))
    print num


def printTupleHelp():
    # 元组循环
    num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    for i in num:
        for j in i:
            print j


def main():
    printTupleHelp()


if __name__ == '__main__':
    main()
