#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-23 12:14 
# user: linux
# description: 常见的数据结构的时间复杂度，通过特定的模块来测试一小段Python代码的执行速度，这里需要使用timeit模块
# timeit:是用来测试小段代码执行速度的类，其中 stmt参数是要测试的代码语句；
#   ；
import timeit


def list_addition():
    number_1 = []
    for I in range(10000):
        number_1 += [I]


def list_append():
    number_1 = []
    for I in range(10000):
        number_1.append(I)


def list_builder():
    number_1 = [I for I in range(10000)]


def list_conversion():
    number_1 = list(range(10000))


def list_extend():
    number_1 = []
    for I in range(10000):
        # extend: 用于将可迭代对象里面的元素都添加到列表中
        number_1.extend([I])


def list_insert():
    number_1 = []
    for I in range(10000):
        number_1.insert(0, I)


# 构造测试类

def main():
    number_1_time = timeit.Timer("list_addition()", "from __main__ import list_addition")
    print "addition:", number_1_time.timeit(1000), "seconds"

    number_1_time = timeit.Timer("list_append()", "from __main__ import list_append")
    print "append:", number_1_time.timeit(1000), "seconds"

    number_1_time = timeit.Timer("list_builder()", "from __main__ import list_builder")
    print "builder:", number_1_time.timeit(1000), "seconds"

    number_1_time = timeit.Timer("list_conversion()", "from __main__ import list_conversion")
    print "conversion:", number_1_time.timeit(1000), "seconds"

    number_1_time = timeit.Timer("list_extend()", "from __main__ import list_extend")
    print "extend:", number_1_time.timeit(1000), "seconds"

    number_1_time = timeit.Timer("list_insert()", "from __main__ import list_insert")
    print "insert:", number_1_time.timeit(1000), "seconds"


if __name__ == "__main__":
    main()
