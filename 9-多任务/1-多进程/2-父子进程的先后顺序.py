# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 多进程：
#   该脚本讨论父子进程的先后顺序
#   按照一般的理解，父进程应该等待子进程执行结束后，结束执行，但是按照下面的顺序，本质上是没有等待的；
#   需要让父进程等待子进程结束后，父进程执行,通过join()方法来实现父进程等待子进程执行；

import multiprocessing
import time
import os


def run(message):
    print "slave: {} start: {}".format(os.getpid(), message)
    time.sleep(5)
    print "slave: {} ended".format(os.getpid())


def main():
    print "master: {}  start ".format(os.getpid())
    multiRun = multiprocessing.Process(target=run, args=('this is son progress',))
    multiRun.start()
    # 主进程执行自己的代码
    multiRun.join(timeout=30)
    print "master: {} ended".format(os.getpid())


if __name__ == '__main__':
    main()
