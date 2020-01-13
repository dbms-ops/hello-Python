# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
#
# 进程间通信的几种方式：
#   ；
#
import time
from multiprocessing import Process, Queue
import os


def write(transfer):
    print 'start write: {}'.format(os.getpid())
    for message in ['A', 'B', 'C', 'D']:
        transfer.put(message)
        time.sleep(0.3)
    print 'stop write: {}'.format(os.getpid())


def read(transfer):
    print 'start read: {}'.format(os.getpid())
    while True:
        value = transfer.get(True)
        print value

    # print 'stop read: {}'.format(os.getpid())


def main():
    transfer = Queue()
    pw = Process(target=write, args=(transfer,))
    pr = Process(target=read, args=(transfer,))

    pw.start()
    pr.start()
    pw.join()

    # pr进程是个死循环，无法等待其结束，只能够强行结束
    pr.terminate()

    print 'parent:{} ended'.format(os.getpid())


if __name__ == '__main__':
    main()
