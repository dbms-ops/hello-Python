# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
#
# 多继承：表示子类继承自多个父类
#   Father <<<------- Child
#   Mother <<<------- Child

# 声明 Fahter

class Father(object):
    def __init__(self, pocket):
        self.pocket = pocket

    def play(self):
        print "play son"

    def func(self):
        print "func"


# 声明母类

class Mother(object):
    def __init__(self, food):
        self.food = food

    def eat(self):
        print "eat"

    def func(self):
        print "func2"


# Child 继承两个父类：Father，Mother

class Child(Father, Mother):

    # 多继承的初始化，分别调用两个父类的初始化函数来完成子类的初始化
    def __init__(self, pocket, food):
        Father.__init__(self, pocket)
        Mother.__init__(self, food)


def main():
    tom = Child(1000, "orange")
    print tom.pocket
    print tom.food
    # 父类中的方法名相同，默认调用的是在括号中排前面的父类中的方法
    # tom.func()调用的是Father的func方法
    tom.func()


if __name__ == "__main__":
    main()
