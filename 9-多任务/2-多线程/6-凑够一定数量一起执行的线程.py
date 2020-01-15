# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# 凑够一定数量才能够一起执行的线程: Python 的 2.7 版本没有对应的barrier, 只有版本大于3才能够执行
#
#

import threading
import time

# 必须达到指定的线程数量后，才执行
bar = threading.Barrier(2)


def run():
    print threading.current_thread().name, "start "
    time.sleep(0.3)
    bar.wait()
    print threading.current_thread().name, "end "


def main():
    for I in range(5):
        threading.Thread(target=run).start()


if __name__ == '__main__':
    main()
