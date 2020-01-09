# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
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



def main():
    combination_help()


if __name__ == '__main__':
    main()
