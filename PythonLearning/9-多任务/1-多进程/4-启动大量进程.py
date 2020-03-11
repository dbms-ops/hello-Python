# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 同时需要启动大量进程，
#
#
#

import os
import time
from multiprocessing import Pool


def run(name):
    print 'son: {} pid: {} start'.format(name, os.getpid())
    # print time.time()
    # print 'son: {} pid: {} ended'.format(name, os.getpid())
    time.sleep(0.3)


def main():
    print 'father: {} start '.format(os.getpid())
    multiproce = Pool()
    # 通过循环一次性启动多个进程
    for i in range(10):
        # 对于同一个函数创建多个进程,并且放入进程池，统一管理
        multiproce.apply_async(run, args=(i,))
    # 使用进程池，在调用join之前，必须先调用close，调用close之后不能够在添加新的进程
    multiproce.close()
    # 进程池对象调用join，需要等到进程池中的所有的子进程结束后，再去执行父进程
    multiproce.join()

    print 'father: {} ended '.format(os.getpid())


if __name__ == '__main__':
    main()
