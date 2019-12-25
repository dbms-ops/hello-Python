# coding=utf-8
#
# 
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# 
#
#
# 可迭代对象：
#   可以直接作用于 for 循环的对象称为可迭代对象，通过isinstance()判断是否是可迭代对象
#   1、集合类数据类型：list、tuple、dict、set、string
#   2、general，包括生成器和带yield的generator function

from collections import Iterable
from collections import Iterator


print isinstance([], Iterable)
print isinstance((), Iterable)
print isinstance('', Iterable)
print isinstance((x for x in range(10)), Iterable)
print isinstance(1, Iterable)

# 迭代器：
#   1、作用于for循环
#   2、被next()函数调用，并且返回下一个值，直到返回异常：StopIteration
# 总结：
#   可以被next函数调用，并且不断返回下一个值的对象称为迭代器


print isinstance([], Iterator)
print isinstance((), Iterator)
print isinstance(1, Iterator)

num = (x for x in range(10))
print next(num)
print next(num)

# Iterator 转换
# 列表转换
print isinstance(iter([1,2,3,4,5]),Iterator)

# 元组转换
print isinstance(iter((1,2,3,4,5)),Iterator)

# set转换
print isinstance(iter({1,2,3,4,5}),Iterator)

# string转换
print isinstance(iter("string"),Iterator)

#

