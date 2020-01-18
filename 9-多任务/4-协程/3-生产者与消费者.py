#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-18 14:35 
# user: linux
# description: 利用协程来实现生产者与消费者模型
# 


def producer(c):
    c.send(None)
    n = 0
    for i in range(5):
        print "Producer produces data: {}".format(i)
        # send 需要发送的是一个字符串，而不是一个整数类型
        r = c.send(str(i))
        print "Consumers consume data: {}".format(r)
    c.close()


def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print "Consumers consume data: {}".format(n)
        data = '200'


def main():
    tom = customer()
    producer(tom)


if __name__ == "__main__":
    main()
