# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 这个文件是一个封装的多进程类
#
#
from multiprocessing import Process
import os


class osProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print 'son: {} start: {}'.format(self.name, os.getpid())

        print 'son: {} ended: {}'.format(self.name, os.getpid())


def main():
    check = osProcess('test')
    check.start()
    check.join(timeout=11)


if __name__ == '__main__':
    main()
