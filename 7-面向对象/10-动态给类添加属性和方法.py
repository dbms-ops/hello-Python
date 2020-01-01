# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 动态给类添加属性和方法
#
#
from types import MethodType


# 创建空类

class Person(object):
    __slots__ = ("name","age","speak")
    pass

tom = Person()

# 动态添加属性和方法，是动态语言的特点
# 动态添加属性
tom.name = "tom"
print tom.name

# 动态添加方法
# 动态添加方法需要引入模块：MethodType

def say(self):
    print "my name is {}".format(self.name)
tom.speak = MethodType(say, tom)

tom.speak()

# 限制给对象动态添加的属性
# 在定义类的时候，定义一个特殊的属性(__slot__),可以用于限制动态添加的属性
# 下面添加的属性是被限制的
tom.height = 91
print tom.height
