# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
# author: linux
# 异常处理：
#   程序运行过程中遇到的会导致程序崩溃的异常；
#   程序在运行过程跳过错误，继续向下执行；
#   try:
#       语句
#    except as e：
#       语句
#    except as e：
#       语句
#    else：
#       语句
#
#   1、当程序执行到 try语句中代码块出现错误，会匹配第一个错误码，如果匹配到，就执行对应的语句
#   2、如果没有 exception 铺捉到异常，异常向上抛出
#   3、如果没有出现错误，执行else中的代码块

try:
    print 4/0
except (NameError,ZeroDivisionError):
    print "Error except"


try:
    print 4/0
except ZeroDivisionError as e:
    print 'Error except'




if __name__ == '__main__':
    pass
    