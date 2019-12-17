# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# author: Lixun
#
# 多行注释
'''
1.多行注释
2.代买不应该有中文字符
3.
'''

# 函数：print  用于将内容进行输出

print "Give a dog a bad name and hang him", "Seeing is believing", "Easy come, easy go"
print 12, 23, "Empty vessels make the most sound", 12 + 23, "Empty vessels" + "make the most sound"
print "12+23", 12 + 23

# 函数：INPUT: 从外部获取变量的值，等待输入并且阻塞

# age = input("please input your age: ")
# print "age = ", age

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


# 常量：程序运行期间不能够改变的数据

# 变量：数字
#   分类：
#       1.整数：处理任意大小的整数[正整数、负整数]
#       2.浮点数：
#       3.复数：
#
age, num = 1, 2
print age, num




# 关键字查看
import keyword

print len(keyword.kwlist)

if __name__ == '__main__':
    pass
