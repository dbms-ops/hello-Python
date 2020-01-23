#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-23 10:50 
# user: linux
# description: 通过枚举法实现 a^2 + b^2 = c^2 且 a + b + c = 1000
#
# 算法的执行效率：
#   1、时间衡量算法的效率
#   2、算法复杂度衡量算法的效率；
#   3、；

import time


def enumeration_for():
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a + b + c == 1000 and a * a + b * b == c * c:
                    print "you need is a:{} b:{} c:{}".format(a, b, c)


# 计算：1000 * 1000 * 1000 * 2
# 2N^3
#

# 程序的执行流程：
# 顺序：顺序结构采用加法进行计算；
# 条件：时间复杂度取最大值；
# 循环：循环结构进行乘法计算；
# ；


def enumeration_for_1():
    # 对于上面的方式进行优化可以极大的极高执行效率
    for a in range(1001):
        for b in range(1001):
            if a * a + b * b == (1000 - a - b) ** 2:
                print "you need is a:{} b:{} c:{}".format(a, b, (1000 - a - b))


def main():
    start_time = time.time()
    enumeration_for_1()
    end_time = time.time()
    print end_time - start_time


if __name__ == "__main__":
    main()
