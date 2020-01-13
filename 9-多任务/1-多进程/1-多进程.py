# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 多进程：
#   进程是系统中程序执行和资源分配的基本单位，每个进程都有自己的数据段、代码段、和堆栈段；
#   借助于multiprocessing实现多进程，本质上是一个跨平台的，在Linux和Windows上面都是可以实现的；
#   该模块提供了一个Process类实现多进程；
# 该脚本可以作为多进程文本文件的参考
#
#

import multiprocessing
import time
import os


# 子进程需要执行的代码
def run(message):
    while True:
        print 'master:{} --> slave:{} do  something: print {}'.format(os.getppid(), os.getpid(), message)
        time.sleep(1.2)


def main():
    print 'master start '
    # 创建一个进程
    multiRun = multiprocessing.Process(target=run, args=('this is son progress',))
    # 启动进程
    multiRun.start()
    # 主进程执行自己的代码
    while True:
        print 'master:{} do what you do'.format(os.getpid())
        time.sleep(1.25)


if __name__ == '__main__':
    main()
