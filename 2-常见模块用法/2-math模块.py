#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#

# math模块的常见用法，math操作不适用于复数，对于复数使用cmath

import math

# 对于浮点数,进行四舍五入操作
print math.ceil(10.123), math.ceil(9.67), math.ceil(9.50), math.ceil(-9.50)

# 绝对值
print math.fabs(-10), math.fabs(10), math.fabs(-0), math.fabs(-11)

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
