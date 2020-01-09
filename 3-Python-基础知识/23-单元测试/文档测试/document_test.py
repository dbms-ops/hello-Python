# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# 文档测试
#   文档测试是写在文件里面的;
# doctest 可以提取注释中的代码执行;
#   该模块严格按照Python的交互式模式提取代码和参数;
import doctest


def little_sum(x, y):
    '''
    add x and y
    :param x: first number
    :param y: second number
    :return: sum

    example:
    >>> print little_sum(1, 3)
    4
    '''

    return x + y


def main():
    # 开始进行文档测试
    doctest.testmod()


if __name__ == '__main__':
    main()
