#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: 高阶函数：map && reduce 的区别
#

# 高阶函数主要是两个：map 与 reduce
#  map(fn,lsd)：
#       fn: 表示是一个函数名称；
#       lsd：表示一个参数序列；
#   用于将传入的函数一次作用在序列中的每一个元素，并且将结果作为一个新的 Iterator 返回；
#  reduce(fd,lsd)：
#       fn: 表示一个函数名
#       lsd：表示一个列表;
#   将函数作用在序列上，该函数必须接受两个参数，reduce把结果继续和序列的下一个元素累计计算
#   例如reduce(f,[a,b,c,d])----> f(f(f(a,b),c),d)；
#

from functools import reduce


# map函数的简单应用，通过函数将一个序列从字符串变为整数
# 将单个字符转换成为对应的字面量整数
def chr2int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]


def map_char2int(fd):
    num = ['2', '3', '5', '6', '7', '8', '9']
    res = map(fd, num)
    print res


# reduce 计算元素的和
def sum_simple(x, y):
    return x + y


def reduce_sum(fn):
    print reduce(sum_simple, [1, 2, 3, 4, 5, 5, 7, 9])


# map and reduce 通常是结合起来使用的
# 例如：实现将字符串转换成为字面量数字
def str2int(string):
    def fc(x, y):
        return x * 10 + y

    def fs(char):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]

    return reduce(fc, map(fs, string))


def main():
    print str2int("1234567")


if __name__ == '__main__':
    main()
