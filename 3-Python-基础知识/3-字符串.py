# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

#
# 字符串
# 字符串是一单引号或者双引号引用的任意文本

# 引号本身并不属于字符串内容
#

# 字符串创建
proverb1 = "see it all"
proverb2 = "Love is a carefully designed lie"

# 字符串运算
#   字符串拼接
print proverb1 + proverb2, '\n', proverb1, proverb2

#   输出重复字符串
print proverb2 * 3

#   查找字符、字符串
print proverb2[0], '\n', proverb2[11], '\n', proverb2[21]

#   截取字符串
print proverb2[0:11], '\n', proverb2[0:-1], proverb2[0:-2], '\n', proverb2[0:-1]

#   in、not in 结合字符串判断
print "see" in proverb1, "see  " in proverb1

#   

if __name__ == '__main__':
    pass
