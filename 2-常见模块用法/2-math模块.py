#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#

# math模块的常见用法，math操作不适用于复数，对于复数请使用cmath

import math

# 对于向上取整
print math.ceil(10.123), math.ceil(9.67), math.ceil(9.50), math.ceil(-9.50)

# 向下取整
print math.floor(11.1112121)

# 返回整数部分与小数部分
print math.modf(12.111213)

# 开方
print math.sqrt(16)

# 绝对值
print math.fabs(-10), math.fabs(10), math.fabs(-0), math.fabs(-11), abs(-10), abs(11)

# 计算阶乘:传递的参数不允许是负数，或者是非整数
print math.factorial(11)

# 接受一个浮点数，用于向上或者向下进行取整操作
print math.ceil(10.123), math.ceil(9.67), math.ceil(9.50), math.ceil(-9.50)

# 用于计算浮点数的余数
print math.fmod(11.0, 3.0)

# 判断浮点数是正数还是负数
print math.isinf(12.00), math.isinf(-11.02)

# 几个常见的常量
print math.pi, math.e



# 数学函数
# 找出最大值
print max(1, 2, 3, 4, 5, 6, 7, 8, -10)

# 返回最小值
print min(1, 2, 3, 4, 5, 7, -10)

# 求X的n次方
print pow(2, 1.2), pow(2, 3), pow(11, 2)

# 四舍五入
print round(3.456, 2), round(3.45678, 3)

#
