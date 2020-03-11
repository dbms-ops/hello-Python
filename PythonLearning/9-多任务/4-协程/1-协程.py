#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-16 09:35 
# user:
# description: 子程序或者子函数在所有语言中都是层级调用的，函数调用是通过栈实现的，一个线程就是一个子程序；
# 协程：
#   类似子程序，在执行过程中，在子程序的内部可中断，中断，去执行别的子程序，不是函数调用，类似CPU中断；
#   协程类似于线程的执行，但是协程本质上是一个线程在执行；
# 协程优点：
#   1、协程的执行效率极高，只有一个线程，不存在变量的冲突；
#   2、协程中共享变量不加锁；
# Python对于协程的支持是通过generator来实现的；
#


def run():
    print '1'
    yield 10
    print '2'
    yield 20
    print '3'
    yield 30


def main():
    # 协程最简单的风格，用于控制函数阶段的最简单执行，用于节约线程或者进程的切换；
    # 得到的返回值是一个生成器
    m = run()
    print next(m)
    print next(m)
    print next(m)


if __name__ == "__main__":
    main()
