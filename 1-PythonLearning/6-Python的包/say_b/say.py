# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
#
# 一个模拟自定模块的功能的模块linux
# 一个 Py文件就是一个可以调用和使用的功能模块


def sayhello():
    print "say hello say_b"


def saynice():
    print "say nice say_b"


def saygood():
    print "say good say_b"


# __name__ 属性：
# 模块本身是一个可执行的py文件，一个模块被另一个程序引用，当需要不执行模块中的某些代码，使用__name__属性，仅仅调用模块中的某一个部分
# 每一个模块都有一个__name__属性
#   1、当执行当前模块的时候，执行__name__属性中的语句
#   2、当模块被调用的时候，仅仅执行被调用的部分
#   3、如果当前文件为程序执行的入口文件，则__name__属性的值为__main__

if __name__ == "__main__":
    print "should not print this statement"

