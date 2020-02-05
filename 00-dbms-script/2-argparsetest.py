#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-24 10:21
# user: linux
# description: 用于测试简单的 argparse 模块功能
#
import sys
import argparse


def cmd():
    args = argparse.ArgumentParser(description='Personal Information ', epilog='Information end ')
    args.add_argument("name", type=str, help="Your name")
    args.add_argument("birth", type=str, help="birthday")
    args.add_argument("-r", '--race', type=str, dest="race", help=u"民族")
    args.add_argument("-a", "--age", type=int, dest="age", help="Your age", default=0, choices=range(100))
    args.add_argument('-s', "--sex", type=str, dest="sex", help='Your sex', default='male', choices=['male', 'female'])
    args.add_argument("-p", "--parent", type=str, dest='parent', help="Your parent", default="None", nargs='*')
    args.add_argument("-o", "--other", type=str, dest='other', help="other Information", required=False, nargs='*')
    args = args.parse_args()  # 返回一个命名空间,如果想要使用变量,可用args.attr
    print "argparse.args=", args, type(args)
    print 'name = %s' % args.name
    d = args.__dict__
    for key, value in d.iteritems():
        print '%s = %s' % (key, value)


if __name__ == "__main__":
    cmd()