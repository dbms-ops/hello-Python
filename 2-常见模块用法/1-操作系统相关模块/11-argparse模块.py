# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

# argparse:
#   用于进行命令行参数解析的强大工具
#


import argparse

def parser_simple():
    # 创建一个参数解析实例
    # 传递命令行参数：
    #    /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py --help
    # 输出：
    #   usage: 11-argparse 模块.py [-h]
    #
    #   optional arguments:
    #       -h, --help  show this help message and exit

    parser = argparse.ArgumentParser()
    parser.parse_args()

def add_positional():
    # 定义一个位置参数
    # [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py --help
    # usage: 11-argparse模块.py [-h] echo
    #
    # positional arguments:
    #   echo
    #
    # optional arguments:
    #   -h, --help  show this help message and exit
    # [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py foo
    # foo

    parser = argparse.ArgumentParser()
    parser.add_argument('name',help="please input your name")
    args = parser.parse_args()
    print type(args)
    print args.__dict__['name'] # 这里使用字典获取对应的参数以及其值


def positional_square():
    # 进行一个乘法运算
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py 11111
    #   123454321
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('square',help="display a square of a given number",type=int)
    args = parser.parse_args()
    print args.square ** 2
    print args.__str__() # 通过字符串获取其值
    print args.__dict__  # 通过字典获取其值


def add_optional():
    # 添加一个可选参数
    #
    # 例如：
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py  --verbosity 12
    #   verbosity turned on
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py  --verbosity
    #    usage: 11-argparse模块.py [-h] [--verbosity VERBOSITY]
    #    11-argparse模块.py: error: argument --verbosity: expected one argument
    #   1、使用--verbosity必须制定一些值

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity",help="increase output verbosity")
    args = parser.parse_args()
    if args.verbosity:
        print "verbosity turned on"


def verbosity_store_true():
    # 只接受两个参数True和False的可选参数
    #   上面的例子接受任意的整型参数
    #   下面的例子只接受True或者False
    # 传递该参数就是True：
    # [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py  --verbose
    #  verbosity turned on
    # 否则就是False
    # [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py
    #

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose",help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print "verbosity turned on"
    print args.verbose



def add_sub_options_optional():
    # 对于上面的例子添加短选项
    # 输出：
    # [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py --h
    # usage: 11-argparse模块.py [-h] [-v]
    #
    # optional arguments:
    #   -h, --help     show this help message and exit
    #   -v, --verbose  increase output verbosity


    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose",help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()
    if args.verbose:
        print "verbosity turned on"
    print args.verbose

def store_true():
    # 结合位置参数和可选参数的输出
    #
    # 例如：
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py 12
    #   144
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py 12 -v
    #   the square of 12 equals 144
    #   1、注意顺序无关紧要
    #   2、


    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print "the square of {} equals {}".format(args.square, answer)
    else:
        print answer
    print args.__dict__


def squre_simple():
    # 传递给 verbosity 一个多值参数，并且根据多值参数进行输出
    # 例如：
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py -v 2 3
    #   the square of 3 equals 9
    #   [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py -v 1 3
    #   3^2 == 9
    #   限制可选参数的范围：
    #    [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py -v 12 2
    #    usage: 11-argparse模块.py [-h] [-v {0,1,2}] square
    #    11-argparse模块.py: error: argument -v/--verbosity: invalid choice: 12choose from 0, 1, 2)


    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", type=int,choices=[0,1,2],
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print "the square of {} equals {}".format(args.square, answer)
    elif args.verbosity == 1:
        print "{}^2 == {}".format(args.square, answer)
    else:
        print answer
    print args.__dict__
    print args.__str__()



def verbosity_and_count():
    # 引入另一个动作参数count：
    #   用于支持：
    #   -v：
    #   -vv：
    #   -vvv：
    #   输出不同的详细信息
    #   count:用于统计 -v 出现的次数
    #
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display the square of a given number")
    parser.add_argument("-v", "--verbosity", action="count",default=0,
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity >= 2:
        print "the square of {} equals {}".format(args.square, answer)
    elif args.verbosity >= 1:
        print "{}^2 == {}".format(args.square, answer)
    else:
        print answer
    print args.__dict__


def squre_and_verbosity():
    # 更加强大的程序运算功能
    #  [root@localhost 2-常见模块用法]# /data1/Python2.7.4/bin/python2.7 ./11-argparse模块.py 3 3 -vv
    #  3 to the power 3 equals 27
    #
    #

    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="show the result of x^y")
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbosity >= 2:
        print "Running '{}'".format(__file__)
    if args.verbosity >= 1:
        print "{}^{} ==".format(args.x, args.y),
    print answer
    # 通过字典来获取参数列表
    print args.__dict__
    # 通过args来获取参数列表：
    #   对于位置参数：通过args.x 直接获取
    #   对于可选参数：通过args.常选项名来获取参数结果
    print args.x, args.y, args.verbosity








def add_mutually_exclusive():
    # 冲突的选项
    #   例如--verbose 与 --quiet 属于相互矛盾的选项
    #
    parser = argparse.ArgumentParser(description="description: calculate X to the power of Y", add_help=True)
    #   description:
    #   version:
    #   add_help:
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    args = parser.parse_args()
    answer = args.x ** args.y

    if args.quiet:
        print answer
    elif args.verbose:
        print "{} to the power {} equals {}".format(args.x, args.y, answer)
    else:
        print "{}^{} == {}".format(args.x, args.y, answer)
    print args

def main():
    add_mutually_exclusive()




if __name__ == '__main__':
    main()
