# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 运算符重载
#
#

print 1 + 2
print "1" + "2"

class Person(object):

    def __init__(self,num):
        self.num = num

    # 运算符重载
    # 对象相加，默认执行__add__运算
    def __add__(self, other):
        return Person(self.num + other.num)

    def __str__(self):
        return "num = {} ".format(str(self.num))


tom = Person(1)
jerry = Person(2)
print tom + jerry

