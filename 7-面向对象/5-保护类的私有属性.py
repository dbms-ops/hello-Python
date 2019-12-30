# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# 类的某些私有属性是不应该在类的外面被访问的
# 

class Person(object):
    # 定义属性：本质上就是在定义变量,这里的变量是以下的方法所公用的，特例在具体的方法中声明

    def __init__(self, name, age, weight, height, money):  # 函数在创建对象的时候，自动执行
        self.name = name  # 使用构造函数的参数列表初始化类属性
        self.age = age
        self.weight = weight
        self.height = height
        # 类的私有属性，例如money是不应该在类的外面被访问的,通过变量名前加上__来实现,
        self.__money = money # 重命名为self._Person__money

        print "You can't see me,add"
        print self.__money
    def money(self):
        print self.__money

    # 通过添加内部的方法来使用内部的属性
    def getmoney(self):
        print self.__money
    def setmoney(self,money):
        if self.__money < money:
            self.__money = money
        print self.__money

tom = Person("tom", 11, 120, 30, 11000)
# 这种方式类似于添加了一个名为__money的属性，并不是在访问类里面的__money属性
tom.__money = 101
tom.money()
print tom.__money

# 通过类添加的方法来操作类里面的函数
tom.setmoney(30000)
tom.getmoney()

# 不能够直接访问tom.__money的原因是因为Python解释器把__money重命名为_Person_money
tom._Person__money = 10
print tom._Person__money

# 在Python中，还存在 _变量，按照约定的规则，表示虽然可以被访问，但是不建议这么做，请把这个变量当做私有变量，不要直接访问

if __name__ == '__main__':
    pass
