# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# 在线程里面使用全局变量的值，但是影响其他线程使用全局变量的值
# 通过threading.local:可以实现为每一个线程绑定一个 '局部变量'
#   ;
import threading

num = 100
# 创建一个全局的threadingLocal对象，每个线程拥有独立的存储空间
# 每个线程都可以对于ThreadingLocal对象进行读写，但是互不影响
local = threading.local()


def run(x, n):
    x = x + n
    x = x - n
    return x


def func(n):
    # 每个线程都有自己的local.x, 类似线程的 '局部变量'
    local.x = num
    for I in range(1000000):
        run(local.x, n)

    print threading.current_thread().name, local.x
    print num


def main():
    t_1 = threading.Thread(target=func, args=(6,))
    t_2 = threading.Thread(target=func, args=(6,))
    t_1.start()
    t_2.start()
    t_1.join()
    t_2.join()


if __name__ == '__main__':
    main()
