# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020-1-16 16:57
# user: Administrator
# description: 可迭代对象的相关知识
#


# 可迭代对象：
#   可以直接作用于 for 循环的对象称为可迭代对象，通过isinstance()判断是否是可迭代对象
#   1、集合类数据类型：list、tuple、dict、set、string
#   2、general，包括生成器和带yield的generator function

from collections import Iterable
from collections import Iterator


def is_Iterable():
    print isinstance([], Iterable)
    print isinstance((), Iterable)
    print isinstance('', Iterable)
    print isinstance((x for x in range(10)), Iterable)
    print isinstance(1, Iterable)
    print isinstance([], Iterator)
    print isinstance((), Iterator)
    print isinstance(1, Iterator)


# 迭代器：
#   1、作用于for循环
#   2、被next()函数调用，并且返回下一个值，直到返回异常：StopIteration
# 总结：
#   可以被next函数调用，并且不断返回下一个值的对象称为迭代器


def next_help():
    num = (x for x in range(10))
    print next(num)
    print next(num)


# Iterator 转换

def list_to_iter():
    # 列表转换
    print isinstance(iter([1, 2, 3, 4, 5]), Iterator)


def tuple_to_list():
    # 元组转换
    print isinstance(iter((1, 2, 3, 4, 5)), Iterator)


def set_to_list():
    # set转换
    print isinstance(iter({1, 2, 3, 4, 5}), Iterator)


def string_to_list():
    # string转换
    print isinstance(iter("string"), Iterator)


def main():
    string_to_list()


if __name__ == '__main__':
    main()
