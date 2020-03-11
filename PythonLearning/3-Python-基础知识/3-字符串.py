# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/16 16:57
# user: Administrator
# description: 常见数据类型：字符串介绍
#

#
# 字符串
# 字符串是单引号或者双引号引用的任意文本

# 引号本身并不属于字符串内容
#


def Create_string():
    # 字符串创建
    proverb1 = "see it all"
    proverb2 = "Love is a carefully designed lie"
    print proverb1, proverb2


def String_concatenation():
    # 字符串运算
    # 字符串拼接
    proverb1 = "see it all"
    proverb2 = "Love is a carefully designed lie"
    print proverb1 + proverb2, '\n', proverb1, proverb2


def String_duplication():
    # 输出重复字符串
    proverb2 = "Love is a carefully designed lie"
    print proverb2 * 3


def String_lookup():
    # 查找字符、字符串
    proverb2 = "Love is a carefully designed lie"
    print proverb2[0], '\n', proverb2[11], '\n', proverb2[21]


def String_interception():
    # 截取字符串
    proverb2 = "Love is a carefully designed lie"
    print proverb2[0:11], '\n', proverb2[0:-1], proverb2[0:-2], '\n', proverb2[0:-1]


def String_judgment():
    # in、not in 结合字符串判断
    proverb1 = "see it all"  # type: str
    print "see" in proverb1, "see  " in proverb1


def main():
    Create_string()
    String_concatenation()
    String_duplication()
    String_lookup()
    String_interception()
    String_judgment()


if __name__ == '__main__':
    main()
