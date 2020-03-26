#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020/1/22 17:54
# user: Administrator
# description: Python 通过模块来支持队列 Queue, 模块在多线程使用过程中：block 和 timeout 都需要合理的设置，否则会导致线程陷入等待
# 
import Queue


# 队列中添加数据
def addQueue():
    ID = Queue.Queue(maxsize=200)
    ID.put('10', block=True, timeout=3)


def getQueue():
    ID = Queue.Queue(maxsize=100)
    ID.put('11', block=True, timeout=3)
    for I in range(10):
        ID.put_nowait(I)
    print ID.get(block=True, timeout=3)
    print ID.get_nowait()
    print ID.get_nowait()


def queueSize():
    ID = Queue.Queue(maxsize=102)
    ID.put('11', block=True, timeout=3)
    for I in range(100):
        ID.put_nowait(I)
    print ID.qsize()


def queueIsEmpty():
    # 队列为空也会抛出异常
    ID = Queue.Queue(maxsize=102)
    ID.put('11', block=True, timeout=3)
    for I in range(100):
        ID.put_nowait(I)
    print ID.empty()
    print ID.not_empty


def queueIsFull():
    # 队列如果为满，会立即抛出异常
    ID = Queue.Queue(maxsize=100)
    ID.put('11', block=True, timeout=3)
    for I in range(100):
        ID.put_nowait(I)
    print ID.full()
    print ID.not_full


def main():
    getQueue()


if __name__ == '__main__':
    main()
