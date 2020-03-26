#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: Python2 系列和Python3 系列的区别
#


def print_difference():
    print "# Python 2 与 Python 3 的区别".title()
    print "# 1、Python 2 的性能比Python 3 的早期版本更加强大"
    print "# 2、Python 3 默认使用 utf-8 进行编码变量命名更加广阔"
    print "# 3、Python 3 去除了 <> 使用 !="
    print "# 4、加入 // 表示整除，Python 2 中 / 表示整除;"
    print "# 5、去除了Print 语句，加入了print()语句，Python 2.6 以后支持改特性；"
    print "# 6、丢弃了 raw_print(),加入新的 input() 函数"
    print "# 7、新的 super() 函数不再需要传递参数，Python 2 里面是必须传递参数的"
    print "# 8、修改了 < 对应行为，不在允许不同类型之间进行转换；"
    print "# 9、Python 2 的字符串是 以 8-bits 字符串进行存储的，Python 3 通过 16 bits 进行存储"
    print "# 10、Python 3 去除了 long 类型，只有一个整数类型 int"
    print "# 11、新增了 Types 类型"
    print "# 12、Python 3 异常捕捉加入了 as 关键字；"
    print "# 13、xrange改名为 range();"
    print "# 14、去除了 file 关键字;"


def main():
    print_difference()


if __name__ == '__main__':
    main()
