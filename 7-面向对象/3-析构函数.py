# coding=utf-8
#
# 
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# 
# 析构函数：
#   __del__(): 释放对象的时候自动调用
#   ；
#
#


class Person(object):
    # 定义属性：本质上就是在定义变量,这里的变量是以下的方法所公用的，特例在具体的方法中声明

    def __init__(self, name, age, weight, height):  # 函数在创建对象的时候，自动执行
        self.name = name  # 使用构造函数的参数列表初始化类属性
        self.age = age
        self.weight = weight
        self.height = height

        print "You can't see me,add"
        # self 代表类的实例，而不是类
        # 那个对象调用方法，那么该方法中的self就代表那个对象;

    # 定义方法：定义函数
    # self:必须是第一参数，代表类的实例，代表第一个对象

    def run(self):
        print "just run"

    def eat(self, food):
        """
        :param food: what you eat
        """
        print " {} eat  {}".format(self.name, food)

    def drink(self, drinks):
        """

        :param drinks: what kind of drinks you drink
        """
        print "{} drink {}".format(self.name, drinks)

    def __del__(self):  # 当对象在被释放的时候被调用
        print "you cand't see me,del"


# tom = Person("tom",11,120,30)

# 手动释放类，调用析构函数
# del tom

# 函数里面定义的对象，会在函数结束时，自动释放，可以减少内存使用
#
def func():
    tom = Person("tom", 11, 120, 30)


func()
