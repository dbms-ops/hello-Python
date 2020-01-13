# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 全局变量在多进程里面是不能够共享的,进程是拥有自己的数据，代码段的
#   ；
#
from multiprocessing import Process
from time import sleep
import os

num = 100


def run():
    print 'slave: {} start'.format(os.getpid())
    # 在子进程中修改全局变量，对于父进程中的全局变量是没有影响的；
    # 在子进程中使用全局变量时，子进程使用了完全不一样的另一份拷贝，父进程和子进程是完全不同的两个变量；
    global num
    num += 1
    print 'run num: {}'.format(num)
    print 'slave: {} end'.format(os.getpid())


def main():
    print "master: {} start".format(os.getpid())

    multiRun = Process(target=run)
    multiRun.start()
    multiRun.join(timeout=10)

    print "num:{}".format(num)
    print "master: {} end".format(os.getpid())


if __name__ == '__main__':
    main()
