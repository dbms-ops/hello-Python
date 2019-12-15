#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#

# random 模块
# 下面总结了以下用法

import random, string

# 用于返回一个 【a，b的一个随机数】
print random.randint(10, 19)

# 产生 0 到 1 之间的随机浮点数
print random.random()

# 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print random.uniform(1.1, 1.54)

# 从序列中随机选取一个元素
print random.choice("tomorrow")

# 生成1 --> 100 的间隔为 2 的随机整数
print random.randrange(1, 100, 2)

# 将序列a中的元素顺序打乱
a = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(a)
print a

# 多个字符中生成指定数量的随机字符
ran_str = ''.join(random.sample('zbcdefghijklmnopqrqw', 5))
print ran_str
# 从a-zA-Z0-9生成指定数量的随机字符
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
print ran_str

#





















