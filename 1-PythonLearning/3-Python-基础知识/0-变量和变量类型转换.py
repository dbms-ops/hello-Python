# !/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: 常见类型的变量输出
#

#
# 多行注释
"""
    1.Multi-line comments
    2.Code should not have Chinese characters
    3.
 """


# 函数：print  用于将内容进行输出
def print_string():
    print "Give a dog a bad name and hang him", "Seeing is believing", "Easy come, easy go"
    print 12, 23, "Empty vessels make the most sound", 12 + 23, "Empty vessels" + "make the most sound"
    print "12+23", 12 + 23


def print_input():
    # 函数：INPUT: 从外部获取变量的值，等待输入并且阻塞
    age = input("please input your age: ")
    print "age = ", age


# 标识符规则：
#   1.只能由字母数字下划线组成
#   2.开头不能够数字
#   3.不能够是Python的关键字[]
#   4.标识符区分大小写
#   5.见名知意
#   6.遵循驼峰原则：grantPrivateSql

# 变量和常量
# 变量：
#   程序可以操作命名空间的名称
#   程序运行期间可以改变的数据
#   变量有自己独特的类型
# 作用：用于将不同类型的数据存入内存
# 变量在使用之前必须定义，否则会出错
# 变量初始化：给予一个空值
def print_variables():
    name = ""
    print name

    # 字符串赋值
    name = "linux"
    print name

    # 类型转换
    number = int(input("please input a num: "))
    print type(number), "the number member address is ", id(number)

    # 删除变量
    # 删除后，变量无法引用
    del name
    # print name


def Constants_And_Variables():
    # 常量：程序运行期间不能够改变的数据

    # 变量：数字
    #   分类：
    #       1.整数：处理任意大小的整数[正整数、负整数]
    #       2.浮点数：
    #       3.复数：
    #
    age, num = 1, 2
    print age, num

    # num1 是一个变量但是引用的是不同的地址，这个说法不是很准确
    num1 = 10
    print id(num1)  # 140666845811600
    num1 = 20
    print id(num1)  # 140666845811360

    # 浮点数
    # 浮点数是由整数部分和小数部分组成
    fnum1 = 1.1
    fnum2 = 2.2
    print fnum1 + fnum2

    # 数字类型转换
    # 浮点型--->整型

    print int(1.1), int(1.9)

    # 整型-->浮点型
    print float(10), float(11)

    # 字符串--->整型
    print int("11122")

    # 字符串--->浮点型
    print float("12.3")

    # + - 作为正号和负号也是可以参与转换的
    print float("-11.2"), int("+11")


# 关键字查看
def print_keyword():
    import keyword

    print len(keyword.kwlist)


# 变量的作用域
#   变量可以使用的范围
#   局部作用域：
#   全局作用域：
#   内建作用域：

def main():
    print_string()
    print_input()
    print_keyword()


if __name__ == '__main__':
    main()
