# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020-1-16 16:57
# user: Administrator
# description: 文件写入操作的流程；
#

#
# 文件内容写入
#  1、首先打开文件

path = "/root/tmp/pycharm_project_179/file.write1"
file_write = open(path, 'w')

# a.将内容写入到缓冲区，等到缓冲区刷新，将内容写入到文件里面，不是立即写入的
file_write.write("A bad penny always turns up. ")

# b.执行缓冲区刷新，将内容写入都按文件里面.
#   缓冲区刷新策略：
#       关闭文件句柄，自动执行刷新
#       缓冲区写入满，自动执行刷新
#       手动刷新缓冲区：
#       遇到 \n 执行自动刷新到缓冲区
file_write.flush()


# 关闭文件句柄
file_write.close()


def main():
    pass


if __name__ == '__main__':
    main()
