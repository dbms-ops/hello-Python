# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# author: linux
# set：
#   无序和无重复的list
#   1、set的对象不能够是可变对象，字典、列表是不能够添加的，但是元组是可以的
#   2、

# 创建set
# 创建set 通过list或者tuple或者dict作为输入集合
# set 可以用于 list tuple，dict元素的去重操作
num = set([1, 2, 1, 2, 3, 4, 5])
print num, type(num)

num = set((1, 2, 3, 23, 41, 2, 4, 1, 5, 1, 2))
print num, type(num)

# 添加元素
num.add(4)
# 添加重复元素是没有效果的
num.add(6)
print num

# 添加列表
# num.add([1, 2, 3, 4])
#
# # 添加字典
# num.add({'name': 1, 'sex': 'f'})
# print num

# 添加元组
num.add((8, 9, 0))
print num

# 插入list、tuple、string
num.update([1, 2, 3, 4, 5])
print num

num.update((9, 10))
num.update('string')
print num

# 删除
num.remove('i')
num.remove('r')
print num

# 循环遍历存取元素
for index, data in enumerate(num):
    print index, data

# set之间的运算
# 交集
num1 = {1, 2, 3, 4}
num2 = set((4, 5, 6, 2))
print num1 & num2
print type(num1)
#

# set最常见的用法是进行数据去重操作


if __name__ == '__main__':
    pass
