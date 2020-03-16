#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-18 14:27 
# user: linux
# description: 协程进行数据传输，通过 data 进行数据传递，但是data的值一直为空，执行yield的返回值是不为空的
# 


def run():
    # 传递空变量,data值始终为空
    data = ''
    r = yield data
    print '1', r, data
    r = yield data
    print '2', r, data
    r = yield data
    print '3', r, data
    r = yield data


def main():
    # 调用m函数
    m = run()
    # 启动 m，这里并没有执行
    print m.send(None)
    # 开始执行 m
    print m.send('a')
    print m.send('b')
    print m.send('c')


if __name__ == "__main__":
    main()
