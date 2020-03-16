# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# commands: 用于执行操作系统命令，并且获取其输出状态
#
#
import commands


def commands_getoutput():
    # 获取执行命令的输出结果，无论成功或者失败
    output = commands.getoutput('pwd &> /dev/null && echo 1')
    print output, type(output)


def commands_get_status_output():
    #  获取输出的状态，以及输出的结果
    status, output = commands.getstatusoutput("touch a")
    print status
    if status:
        print "commands run successful"

    status, output = commands.getstatusoutput("netstat -ntl | grep 3306")
    print status, output
    if not status:
        print "the result is {}".format(output)


def main():
    commands_get_status_output()


if __name__ == '__main__':
    main()
