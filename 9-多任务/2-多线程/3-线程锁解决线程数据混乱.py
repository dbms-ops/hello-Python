# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# 线程锁：
#   用来解决，多个线程操作相同数据出现的数据异常；
# 

import threading

# 创建锁对象

lock = threading.Lock()

num = 0


def thread_1(n):
    global num
    for i in range(1000000):
        # 施加锁
        # 阻止了线程的并发执行，施加锁的代码本质上只能够以单线程的模式执行，效率下降；
        # 锁滥用会导致出现死锁，死锁行为只能够有操作系统检测，并且进行释放；
        lock.acquire()
        try:
            num += n
            num -= n
        finally:
            # 释放锁
            lock.release()


def thread_2(n):
    global num
    for i in range(1000000):
        with lock:
            num += n
            num -= n


def main():
    t_1 = threading.Thread(target=thread_1, args=(6,))
    t_2 = threading.Thread(target=thread_1, args=(9,))
    t_1.start()
    t_2.start()

    t_1.join()
    t_2.join()


if __name__ == '__main__':
    main()
    print num
