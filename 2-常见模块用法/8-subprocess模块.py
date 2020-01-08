# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7


# subprocess模块：用于执行操作系统命令，并且获取对应的结果
# 完善的模块功能需要使用Python3系列来使用
# 该模块不建议在Python2 中使用，建议使用subprocess32

import subprocess


def run_help():
    # 接受字符串或者列表形式的命令，返回命令执行结果和状态码
    result = subprocess.run(['df', '-h'])
    print type(result), result[0], result[1]


def call_help():
    # 执行命令，返回命令执行结果和状态码
    result = subprocess.call(['ls', '-l'])


def check_call_help():
    # 执行命令，返回结果和状态，正常为0；执行错误则抛出异常
    subprocess.check_call(['lm', '-l'])


def getstatusoutput_help():
    # 3接受字符串形式的命令，返回一个元组形式的结果：第一个元素是状态码，第二个为执行结果
    result = subprocess.getstatusoutput('pwd')
    print type(result), result[0], result[1]


def getoutput_help():
    # 3接受字符串形式的命令，返回执行结果
    subprocess.getoutput('pwd')


def check_output():
    # 执行命令，返回运行结果
    res = subprocess.check_output("pwd")
    print res


def call_io_direct_help():
    # 2 支持的功能
    # subprocess.call：用于执行一个操作系统命令
    # 这里将命令的输出进行重定向
    subprocess.call(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 2 subprocess.check_call 用于执行命令，执行成功，返回成功，否则抛出异常


def main():
    call_io_direct_help()


if __name__ == '__main__':
    main()
