# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# author: Lixun
#
# 条件判断语句
#   if 表达式：
#       语句1
#   语句2
#   如果表达式为真，执行语句1
#   否则执行语句2
#
# 多分支if语句
#   if 表达式：
#         语句1
#   else:
#         语句2
#
#   如果表达式为真，执行表达式里面的语句
#   如果表达式为假，跳过if循环，执行后面的语句
# 为假：
#   0 0.0 '' None False
# 为真：
#   其余为真

# 通过下面的方式可以用于判断一个表达式真还是假
if 0:
    print "True"
else:
    print "False"

if 0.0:
    print "true"
else:
    print "False"

if None:
    print "True"
else:
    print "False"


# 判断传递的参数为真还是为假
def trueOrFalse(argument):
    if argument:
        print "true"
    else:
        print "fasle"


trueOrFalse(1)
trueOrFalse(None)
trueOrFalse(0)

if __name__ == '__main__':
    pass
