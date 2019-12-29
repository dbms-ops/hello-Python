# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 重写：将函数重新声明
#  __str__(): 在使用print 打印对象的时候，自动调用，是一个用于描述对象的方法
#  __repr__()；在Python解释器中直接使用对象名，默认调用的方法
#

class Person(object):
    # 定义属性：本质上就是在定义变量,这里的变量是以下的方法所公用的，特例在具体的方法中声明

    def __init__(self, name, age, weight, height):  # 函数在创建对象的时候，自动执行
        self.name = name # 使用构造函数的参数列表初始化类属性
        self.age = age
        self.weight = weight
        self.height = height

        print "You can't see me,add"


    def __str__(self): # 在用户使用print 打印对象时，自动调用
        print "this is __str__()"
        return "this is str {} {} {} {}".format(self.name,self.age,self.weight,self.height)

    def __repr__(self): # 在Python解释器中，使用对象名直接调用的方法
        print "this is __str__()"
        return "this is str {} {} {} {}".format(self.name, self.age, self.weight, self.height)
    # 注意：在没有str且有repr的时候， str = repr
    # 这两个方法用于在一个对象的属性很多，并且需要打印属性的值时，比较有用

tom = Person("tom", 11, 120, 30)

print tom
