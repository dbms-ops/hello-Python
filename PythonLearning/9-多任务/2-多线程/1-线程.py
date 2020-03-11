# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# 多线程：
#   在一个进程内部，要同时干多件事，就需要同时运行多个'子任务'，这些子任务就是线程，线程通常叫做轻型的进程，线程是共享内存空间的并发执行
#   的多任务，每个线程都共享一个进程的资源；
#   线程是最小的执行单元，进程是最小的资源分配单元，进程至少由一个线程组成；
#
# 模块：
#   1、__thread 模块：是一个接近于底层的模块；
#   2、threading：高级模块，对于__threading 模块进行了封装；
#
# description：启用一个多线程，用于实现特定的任务：
#
import threading
import time


def run(num):
    print 'slave {} start'.format(threading.current_thread().name)
    # 线程需要完善的主要功能
    #
    print 'num: {}'.format(num)
    time.sleep(0.3)

    print 'slave {} end'.format(threading.current_thread().name)


def main():
    # 任何进程默认都会启动一个进程、称为主线程，主线程可以启动新的子线程；
    # threading.current_thread: 返回当前实例的一个对象，通过name属性获取名称
    print 'master threading start: {} '.format(threading.current_thread().name)
    # 创建线程
    num = 1
    t = threading.Thread(target=run, name='rootThread', args=(num,))
    t.start()

    # 对于线程，进程需要等待线程结束
    t.join()
    print 'master threading end: {} '.format(threading.current_thread().name)


if __name__ == '__main__':
    main()
