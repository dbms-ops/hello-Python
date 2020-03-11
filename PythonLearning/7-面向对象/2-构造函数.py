# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
#
# 构造函数：
# 格式：__init___:在使用类创建对象的时候，自动进行调用
#   如果不显示的写出构造函数，会默认写出一个空的构造函数，但是什么都不执行；
#

class Person(object):
    # 定义属性：本质上就是在定义变量,这里的变量是以下的方法所公用的，特例在具体的方法中声明

    def __init__(self, name, age, weight, height):  # 函数在创建对象的时候，自动执行
        self.name = name # 使用构造函数的参数列表初始化类属性
        self.age = age
        self.weight = weight
        self.height = height

        print "You can't see me"
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



tom = Person("tom",12,120,30)
tom.run()
tom.eat("noodles")





