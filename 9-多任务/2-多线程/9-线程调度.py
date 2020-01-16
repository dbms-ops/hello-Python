# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/15 20:42
# user: Administrator
# description: 脚本用于实现线程调度功能，实现线程执行顺序的可控性                                                              *
#


import threading

# 线程条件变量

cond = threading.Condition()


def thread_1():
    with cond:
        for i in range(0, 100, 2):
            print threading.current_thread().name, i
            cond.wait()
            cond.notify()


def thread_2():
    with cond:
        for i in range(1, 100, 2):
            print threading.current_thread().name, i
            cond.notify()
            cond.wait()


def main():
    threading.Thread(target=thread_1).start()
    threading.Thread(target=thread_2).start()


if __name__ == '__main__':
    main()
