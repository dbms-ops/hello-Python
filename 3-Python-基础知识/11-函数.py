# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# author: Lixun

# 代码模块化：
#  函数：
#   1、在一个完整的项目中，某些重复使用的功能会被封装成函数，避免代码重复
#   优点：
#       1、简化代码的结构，降低代码的复用度
#       2、对于某些功能的修改，只需要修改某些函数即可
#

# 定义函数：
#   def 函数名(参数列表)：
#       语句1
#       return 表达式
#

#  def：
#   表示函数关键字;
#   函数名遵循标识名规则
#   参数列表：任何传入函数的参数和变量必须在()之间，使用逗号进行分割。函数从函数的调用者获取的信息
#   : 函数的内容该符号开始，并且需要缩进
#   语句：标识函数体，函数封装的功能
#   return 结束函数，并且返回信息给函数的调用者，默认return None
#   表达式：函数返回给调用者的信息
#
# 简单的函数：
#   无参数、无返回值的函数

def toDoList():
    print "toDoList"


# 函数的调用：
#   函数名：函数功能的名称，用来识别并且进行函数调用
#   参数列表：函数调用者传递给函数的信息
#   函数调用的本质是实参给形参传递参数的过程

toDoList()


# 函数的参数：
#   形参：在函数定义时，声明的参数
#   实参：函数在调用的时候，传递的参数，本质是一个值
#

def powerSum(num):
    sum = 0
    if num is not None:
        for I in num:
            sum += I
    return sum
    # 执行完成 return 语句，函数执行结束，后面的语句不再执行


print powerSum([1, 2, 3, 4])


# 参数传递：
#   值传递：
#       传递不可变类型：string、tuple、number；
#
#   引用传递：
#       传递可变类型：list、dict、set属于可变类型，本质上传递是指针
# 本质上就是你传递的值在函数处理之后，是否会发生改变
#

# 关键字参数
#   允许函数调用时，参数的顺序与定义不一致
#
def printmy(name, age):
    print name, age


printmy(age=10, name='Hello Man')


# 默认参数
#   调用函数时，如果没有传递参数，使用默认参数
#   1、定义默认参数，需要将默认参数放到最后

def printmy(name="hello man", age=14):
    print name, age


printmy()
printmy(age=10, name='Hello Man')


# 不定长参数：
#   能够处理比定义时更多的的参数；
#   1、存放所有未命名的变量参数；
#   2、如果在函数调用时，没有传递，默认就是一个空元组；
#


def func(name, *args):
    print name
    for x in args:
        print x


func(1, 2, 3, 4, 5)


# 不定长参数的另一种传递方式
#   1、通过这种方式传递的是一个字典
#   2、传递的是键值对的参数，和*代表的意义是类似的
def func1(**kwargs):
    print type(kwargs)
    print kwargs


func1(x=1, y=2, z=3)


# 接受任意参数
def fun3(*args, **kwargs):
    pass


# 匿名函数
#   匿名函数不使用 def 定义函数，使用 lambda 来定义匿名函数
#   特点：
#       1、lambda只是一个表达式，函数体比def简单；
#       2、实现的逻辑比较简单，主题是一个表达式，而不是代码块
#       3、匿名函数有自己的命名空间，不能够访问自由参数列表之外的或者全局命名空间的参数
#   格式：lambda：参数1，参数2，.....：expression ；

sum = lambda num1, num2: num1 + num2
print sum(1, 13)


# 装饰器
#   本质上是闭包，用于将一个函数作为参数传递给另一个函数，并且返回值是一个函数
#   装饰器就是在对函数进行处理
#
# 声明一个函数：
def test():
    print "More haste, less speed."


# 声明一个装饰器函数来修饰func
def outer(test):
    def inner():
        print "Outer is here, decorator"
        test()

    return inner


# 获取修饰后的函数
f = outer(test)
f()


# 上面的装饰器是学习版本，下面是正式的版本
#


def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)

    return inner


@outer
def sayAge(age):
    print "this is {} years".format(age)


sayAge(-10)


# 比较通用的装饰器
# 支持传递任意参数进行判断
def outer(func):
    def inner(*args, **kwargs):
        pass
        func(*args, **kwargs)

    return inner


#

if __name__ == '__main__':
    pass
