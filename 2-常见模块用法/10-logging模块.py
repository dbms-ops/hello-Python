# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
# author: lixun
# web：https://www.cnblogs.com/yyds/p/6901864.html
# logging 模块：
#   日志是一种可以追踪某些软件运行时所发生事件的方法。一个事件可以用一个可包含可选变量数据的消息来描述。此外，事件也有重要性的概念，
#   这个重要性也可以被称为严重性级别
#  日志的常见等级：
#       DEBUG
#       INFO
#       NOTICE
#       WARNING
#       ERROR
#       CRITICAL
#       ALERT
#       EMERGENCY
#  日志记录的几个内容：
#       事件发生时间
#       事件发生位置
#       事件的严重程度--日志级别
#       事件内容
#  logging 模块的几个日志级别：
#       DEBUG：最详细的日志信息，典型应用场景是 问题诊断
#       INFO：信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
#       WARNING：当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
#       ERROR：由于一个更严重的问题导致某些功能不能正常运行时记录的信息
#       CRITICAL：当发生严重错误，导致应用程序不能继续运行时记录的信息
#  日志级别：DEBUG < INFO < WARNING < ERROR < CRITICAL
#  日志格式：
#       %(asctime)s：日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
#       %(created)f：日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
#       %(relativeCreated)d：日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
#       %(msecs)d：日志事件发生事件的毫秒部分
#       %(levelname)s：该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
#       %(levelno)s：该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
#       %(name)s：所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
#       %(message)s：日志记录的文本内容，通过 msg % args计算得到的
#       %(pathname)s：调用日志记录函数的源码文件的全路径
#       %(filename)s：pathname的文件名部分，包含文件后缀
#       %(module)s：filename的名称部分，不包含后缀
#       %(lineno)d：调用日志记录函数的源代码所在的行号
#       %(funcName)s：调用日志记录函数的函数名
#       %(process)d：进程ID
#       %(processName)s：进程名称，Python 3.1新增
#       %(thread)d：线程ID
#       %(thread)s：线程名称
#
# 对于日志的记录应该分为两种格式：在debug模式下如何记录日志，在程序运行模式下如何记录日志
#
# 一些重要信息：
#   logging.basicConfig()：函数是一个一次性的简单配置工具，多次调用以第一次为准
#   变量传递类似于print，例如：logging.warning('%s is %d years old.', 'Tom', 10)
#   对于logging.DEBUG()等支持三个关键字参数：
#       exc_info: 其值为布尔值，如果该参数的值设置为True，则会将异常异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中
#       stack_info：其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中
#       2.7 暂时不支持上面两个模块
#
#       extra：这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突
#

import logging

# 配置日志的输入格式，支持自己制定字符串
#LOG_FORMAT = "num: %(lineno)d :- %(asctime)s - %(levelname)s - %(message)s"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
# 设置时间格式
DATE_FORMAT = "%m-%d-%Y %H:%M:%S %p"
# DATE_FORMAT = '%Y-%m-%d %H:%M:%S '
logging.basicConfig(filename="/root/Mysql-6379.log", filemode="a", datefmt=DATE_FORMAT, format=LOG_FORMAT,
                    level=logging.DEBUG)
# logging.log(logging.ERROR, "This is a ERROR log")
logging.DEBUG()


# 底下的代码和上面代码分开执行
# 2.7支持extra属性但是不支持exc_info、stack_info两个属性

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s [%(ip)s] - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.warning("Some one delete the log file.", extra={'user': 'Tom', 'ip':'47.98.53.222'})

logging.DEBUG()

#


if __name__ == '__main__':
    pass

import commands