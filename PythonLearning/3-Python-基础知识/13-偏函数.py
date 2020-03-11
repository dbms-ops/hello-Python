# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020-1-16 16:57
# user: Administrator
# description: 偏函数的相关知识
#

# 偏函数：
#  利用原有函数的功能，申明类似的函数，实现简单的功能
#

print int('10010', base=2)


# 偏函数
def int2(string, base=2):
    return int(string, base)


# 利用模块生成偏函数
import functools

int_2 = functools.partial(int, base=2)


def main():
    print int2("1001001")
    print int_2('0010001110')


if __name__ == '__main__':
    main()
