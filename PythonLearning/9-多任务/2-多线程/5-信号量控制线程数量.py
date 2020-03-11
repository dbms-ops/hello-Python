# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# 通过信号量来控制线程数量：用于控制单次几个线程同时执行，这种情况是因为需要执行的线程总数，大于单次执行的线程数量
#
#
import threading
import time

sem = threading.Semaphore(3)


def run():
    with sem:
        for i in range(10):
            print threading.current_thread().name, i
            time.sleep(0.3)


def main():
    for I in range(5):
        threading.Thread(target=run).start()


if __name__ == '__main__':
    main()
