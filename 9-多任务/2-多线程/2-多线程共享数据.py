# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# 多线程：
#   所有变量都由所有的线程共享；
#   所以任何一个变量都可以被任何一个线程共享，线程共享数据的最大危险在于不知道何时修改了这些变量的值；
#   在没有线程锁的情况下，是不能够保证以下脚本的输出为 0 的；
#
import threading

num = 0


def thread_1(n):
    global num

    for i in range(10000000):
        num += n
        num -= n


def thread_2(n):
    num = 10001


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
