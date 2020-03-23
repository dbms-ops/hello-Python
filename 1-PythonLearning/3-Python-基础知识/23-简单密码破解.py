#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: 脚本用于实现简单的密码破解功能
#
# 简单的暴力密码破解
#   使用代码生成排列；
#
import itertools


def arrgement_help():
    mylist = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 6))
    print len(mylist)
    print str(mylist[1])


def combination_help():
    mylist = list(itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 6))
    print len(mylist)


def combination_arrgement_help():
    mylist = list(itertools.product([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], repeat=6))
    print len(mylist)


def pass_four_help():
    passwd = (''.join(x) for x in itertools.product('0123456789', repeat=4))
    print next(passwd)
    print next(passwd)
    print next(passwd)


def main():
    pass_four_help()


if __name__ == '__main__':
    main()