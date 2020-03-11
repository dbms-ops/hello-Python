# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# 定时线程：延迟执行线程
#
#

import threading


def run():
    print 'timer threading test'


def main():
    t = threading.Timer(3, run)
    t.start()
    t.join()
    print 'parent threading ended'


if __name__ == '__main__':
    main()
