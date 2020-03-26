# !/data1/Python2.7/bin/python27
# -*-coding:utf-8-*-
# time: 2020-01-24 10:21
# user: linux
# descriptio： 简单的分支语句

print "你好"

S = 'F'

print "多分支if结构"

if S == 'F':
    print "Gentlemen"
else:
    print "Lady"

print "end"

s = 'M'
c = 'r'

if s != 'M' and c == 'r':
    print i
    print "r Gentlmen"
else:
    print 'Lady'
print "end"

# 单分支if结构

rec = 98
if rec >= 90 and rec <= 100:
    print "Best"
if rec >= 80 and rec <=90:
    print "better"

if rec >= 90 or s == 'M':
    print "M is best"

if rec < 60:
    print "you should improve"

if not rec < 60:
    print "you should not improve"

# 嵌套的If分支

age = 12
gender = "male"
if gender == "male":
    if age > 18:
        print "Gentleman"
    else:
        print "Boy {}".format(age)
else:
    if age > 18:
        print "lady"
    else:
        print "girl"

# 多层嵌套的循环

record = 90  # 用于声明一个分数变量，给出评级
if record >= 60:
    if record >= 70:
        if record >= 80:
            if record >= 90:
                print "you got A"
            else:
                print "You got B"
        else:
            print "You got C"
    else:
        print "You got D"
else:
    print "You got E"









