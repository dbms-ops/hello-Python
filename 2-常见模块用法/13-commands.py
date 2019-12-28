# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# commands: 用于执行操作系统命令，并且获取其输出状态
#
#
import commands

# 获取执行命令的输出结果，无论成功活着失败
output = commands.getoutput('pwd &> /dev/null && echo 1')
print output, type(output)

#  获取输出的状态，以及输出的结果
status, outputtest = commands.getstatusoutput("touch a")
print status
if status:
    print "commands run successful"


