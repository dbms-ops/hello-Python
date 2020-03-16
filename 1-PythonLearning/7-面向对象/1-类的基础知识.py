# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
#
# 创建一个简单额类
#

# 创建类：
# 类本身是一种数据类型，本身不占据内存。通过类是实例化的对象是占据内存空间的
# class 类名(父类列表)
#     属性
#     行为
# object 称为基类，超类，所有类的父类，没有合适的父类的时候，就是object


class Person(object):
    # 定义属性：本质上就是在定义变量,这里的变量是以下的方法所公用的，特例在具体的方法中声明
    name = ''
    age = 10
    height = 120
    weight = 10

    # 定义方法：定义函数
    # self:必须是第一参数，代表类的实例，代表第一个对象
    def run(self):
        print "just run"

    def eat(self, food):
        """
        :param food: what you eat
        """
        print "eat  {}".format(food)

    def drink(self, type):
        """

        :param type: what kind of drink
        """
        print "{} drink {}".format(self.name, type)


# 类实例化对象
# 对象名 = 类名(参数列表)
# 没有参数()不能够省略

tom = Person()
print tom, type(tom), id(tom)

jerry = Person()
print jerry, type(jerry), id(jerry)

# 访问对象的属性和方法
# 添加属性
# 对象名.属性名 = 新值
tom.name = "tom"
tom.age = 12
tom.height = 120
tom.weight = 14
print tom.name, tom.age, tom.height, tom.weight

# 访问方法
# 对象名.方法名(参数列表)
#
tom.drink("orange")
