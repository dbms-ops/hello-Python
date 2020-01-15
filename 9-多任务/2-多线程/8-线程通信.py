# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# 线程通信：
#
#
import threading
import time


def run():
    # 创建事件对象
    event = threading.Event()

    def func():
        for I in range(5):
            # 阻塞等待事件的触发
            event.wait()
            # 表示等待事件触发行为重置
            event.clear()
            print "event threading test start"

    t = threading.Thread(target=func).start()
    return event


def main():
    e = run()
    # 触发事件
    for I in range(5):
        time.sleep(2)
        e.set()


if __name__ == '__main__':
    main()
