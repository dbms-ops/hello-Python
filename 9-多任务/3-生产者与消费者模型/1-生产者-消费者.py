# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# 生产者与消费者模型：
#   通过队列来实现消费者和生产者模型
# 
import Queue
import random
import threading
import time


def producer(i, q):
    for I in range(10):
        num = random.randint(0, 1000)
        q.put(num)
        print "producer: {} product {} put in queue".format(i, num)
        time.sleep(0.5)
    # 生产数据结束
    q.task_done()


def customer(i, q):
    while True:
        if q.qsize() == 0:
            break
        item = q.get(block=True, timeout=2)
        print item
        print 'customer:{} custom {}'.format(i, item)
        time.sleep(0.3)


def main():
    # 创建消息队列
    q = Queue.Queue()
    # 启动生产者
    produce = threading.Thread(target=producer, args=(1, q))
    produce.start()

    time.sleep(2)
    custome = threading.Thread(target=customer, args=(1, q))
    custome.start()

    produce.join(timeout=1)
    custome.join(timeout=1)
    exit(0)


if __name__ == '__main__':
    main()
