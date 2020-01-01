# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 对象属性与类属性
#   对象属性：
#   类属性：表示通过类名来进行调用的属性；
#
#

class Person(object):
    # name：表示的是类属性，本质上是通过类名来进行调用的
    name = "person"
    #
    def __init__(self, name):
        # 对象属性：通过__init__定义的属性称为对象属性，对象属性的优先级是高于类属性的，当没有对象属性的时候，默认使用类属性
        self.name = name


# 通过类名调用类属性
print Person.name

Person.name = "tom"
print Person.name

# 通过对象来调用对象属性
tom = Person("linux")
print tom.name

# 动态的给对象添加属性,添加的对象属性只针对于当前对象生效，对于类创建的其他对象，没有该对象属性
tom.age = 20
print tom.age

# 删除对象中的name属性，会调用同名的类属性
del tom.name
print tom.name

# 对象属性和类属性是不能够重名的，对象属性会屏蔽掉同名的类属性

