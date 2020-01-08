# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

import subprocess32


def run_help():
    # subprocess32.call：执行一个命令，等待执行完成，或者等待超时
    # 这个命令在不进行IO重定向的情况下，错误，正确信息都会默认输出
    subprocess32.run(['ls', '-lh', '/data1/'])
    # print result.stdout


def check_all_help():
    # subprocess32.check_call: 执行一个命令，并且检查返回值，如果为0正常返回
    # 否则抛出：CalledProcessError 异常

    subprocess32.check_call(['ls', '-l'])

    # 执行出错的命令，抛出异常
    try:
        subprocess32.check_call(['ls', '----'])
    except subprocess32.CalledProcessError:
        print "get error"


def check_output_help():
    # subprocess32.check_output: 执行命令，并且将结果通过 byte string的方式进行返回;
    # 对于执行出错的命令，会直接抛出异常
    result = subprocess32.check_output(['ls', '-l', '/data1/'])
    print result, type(result)


def run_io_direct_help():
    # 错误输出到标准输出，重定向需要更改源码
    # 这种方式是比较常用的
    # subprocess32.check_output(['ls','-l non_existent_file ; exit 0'])

    # subprocess32.run 执行一个命令，并且返回一个CompletedProcess对象
    # 包含：
    #   args：
    #   returncode：
    #   stdout：stdout=PIPE: 需要传递这两个参数，才会捕捉
    #   stderr：stderr=PIPE: 将输出的错误信息抛出到PIPE中

    result = subprocess32.run(['ls', '-l', '/data1/'], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE, timeout=10)
    # 参数选项
    print result.args
    # 命令执行的返回值
    print result.returncode
    # 返回的错误信息
    print result.stderr
    # 命令执行的返回信息
    print result.stdout


def list2cmdline():
    # list2cmdline: 把一个命令行序列转换成为命令行字符串，目前没有发现用处
    result = subprocess32.list2cmdline(['-a', 'ba', '-c', 'd'])
    print result


def popen_help():
    # subprocess32用于创建一个进程
    p = subprocess32.Popen("ls -l", shell=True)
    print p.returncode
    print p.wait()
    print p.returncode


def run_test():
    result = subprocess32.run(['/bin/touch', '/root/a.file'], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE,
                              timeout=10)
    # 参数选项
    print result.args
    # 命令执行的返回值
    print result.returncode
    # 返回的错误信息
    print result.stderr
    # 命令执行的返回信息
    print result.stdout

    result = subprocess32.run(['/bin/rm', '-f', '/root/a.file'], stdout=subprocess32.PIPE, stderr=subprocess32.PIPE,
                              timeout=1)
    # 参数选项
    print result.args
    # 命令执行的返回值
    print result.returncode
    # 返回的错误信息
    print result.stderr
    # 命令执行的返回信息
    print result.stdout

    result = subprocess32.run(['/bin/mkdir', '-p', '/data/mongo/mongo-shake'], stdout=subprocess32.PIPE,
                              stderr=subprocess32.PIPE,
                              timeout=1)
    # 参数选项
    print result.args
    # 命令执行的返回值
    print result.returncode
    # 返回的错误信息
    print result.stderr
    # 命令执行的返回信息
    print result.stdout

    result = subprocess32.run(['chown', '-R', 'mongo.mongo', '/data/mongo/mongo-shake'], stdout=subprocess32.PIPE,
                              stderr=subprocess32.PIPE, timeout=1)
    # 参数选项
    print result.args
    # 命令执行的返回值
    print result.returncode
    # 返回的错误信息
    print result.stderr
    # 命令执行的返回信息
    print result.stdout


def main():
    run_test()


if __name__ == '__main__':
    main()
