# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 继承是多态的前提
#  多态是一种事物的多种形态
#

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print "{} eat".format(self.name)


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)


class Mouse(Animal):
    def __init__(self, name):
        super(Mouse, self).__init__(name)


# 定义 Class Person

class Person(object):
    def feedanimal(self, animal):
        print "for you"
        animal.eat()



tom = Cat("tom")
jerry = Mouse("jerry1")
women = Person()
women.feedanimal(tom)
women.feedanimal(jerry)



