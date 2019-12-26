# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

import subprocess32

# subprocess32.call：执行一个命令，等待执行完成，或者等待超时
result = subprocess32.run(['ls', '-ltr', '/data1/'])
print result

# subprocess32.check_call: 执行一个命令，并且检查返回值，如果为0正常返回
# 否则抛出：CalledProcessError 异常

result = subprocess32.check_call(['ls', '-l'])
print result

# 执行出错的命令，抛出异常
try:
    result = subprocess32.check_call(['ls', '----'])
    print result
except subprocess32.CalledProcessError:
    print "get error"

# subprocess32.check_output: 执行命令，并且将结果通过 byte string的方式进行返回
result = subprocess32.check_output(['ls', '-l', '/data/'])
print result, type(result)

# 错误输出到标准输出，重定向需要更改源码
# subprocess32.check_output(['ls','-l non_existent_file ; exit 0'])

# subprocess32.run 执行一个命令，并且返回一个CompletedProcess对象
# 包含：
#   args：
#   returncode：
#   stdout：stdout=PIPE，需要传递这两个参数，才会捕捉
#   stderr：stderr=PIPE

result = subprocess32.run(['ls', '-l', '/data12/'], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE, timeout=10)
print result.args
print result.returncode
print result.stderr
print result.stdout

# list2cmdline: 把一个命令行序列转换成为命令行字符串，目前没有发现用处
result = subprocess32.list2cmdline(['-a', 'ba', '-c', 'd'])
print result

# subprocess32用于创建一个进程
p = subprocess32.Popen("ls -l", shell=True)
print p.returncode
print p.wait()
print p.returncode


import this


if __name__ == '__main__':
    pass













