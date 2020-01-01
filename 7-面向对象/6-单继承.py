# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 单继承与多继承：
#
# 继承：
#   A类：
#   B类：当B类继承自A类的时候，B类就拥有A类的全部属性和方法
#   A是B类的父类，B是A类的子类;
#   object类：该类是所有类的父类，称为基类或者是超类;
# 继承的作用：
# 1、简化代码，减少冗余
# 2、提高了代码的健壮性
# 3、提高了代码的安全性
# 4、继承是多态的前提；
# 继承的缺点：
#  耦合与内聚是用来描述类与类之间的关系的，耦合性越低、内聚性越高，代码越好；
#
#  单继承：
#  类B继承自类A；
#  Person <------ Student

# 对于类的名称，首字母应该大写
class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        # 父类添加私有属性
        self.__money = money

    def run(self):
        print "run"

    def eat(self, food):
        print "eat {}".format(food)

    def setmoney(self, money):
        if money > self.__money:
            self.__money = money

    def getmoney(self):
        print self.__money


class Student(Person):
    # 继承类的初始化，需要使用super(),调用父类的__init__()来初始化子类的
    # 定义学生独特的属性stuID
    def __init__(self, name, age, money, stuid):
        super(Student, self).__init__(name, age, money)
        self.stuid = stuid

    def pocket(self):
        print "get pocket money {}".format(self.__money)


tom = Student("tom", 23, 11234, "G11111")

print tom.age
print tom.name
print tom.stuid
# 这里的错误，说明子类是不会继承父类的私有属性的,
# tom.pocket()

# 对于父类的属性是可以完整继承的;通过继承的公有方法来访问类的私有属性
tom.setmoney(1111234)
tom.getmoney()


# 单继承
# Person <---- Student
# Person <---- Worker

class Worker(Person):
    def __init__(self, name, age, money):
        super(Worker, self).__init__(name, age, money)


print "多继承"
worker = Worker("DBA", 39, 112213)
worker.eat("orange")
