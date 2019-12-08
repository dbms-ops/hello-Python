#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#
# 循环
#

#

print "循环"
#  "判断1--10的偶数和奇数"
i = 1

while i < 10:
    if i % 2 == 0:
        print "{} is even".format(i)
    else:
        print "{} is odd".format(i)
    i += 1

# 计算1 + ... + 100

i = 1
sum = 0
while i < 101:
    sum = sum + i
    i += 1
print "the result is {}".format(sum)

#



# 输出水仙花数:数字本身 = 个位的立方 + 十位的立方 + 百位的立方

i = 100
while i < 1000:
    # 取 百 十 个 位 数
    a = i / 100
    b = i / 10 % 10
    c = i % 100 % 10

    if i == a ** 3 + b ** 3 + c ** 3:
        print i
    i = i + 1

# 嵌套循环
# 输出乘法表的上半部分，或者是下半部分

i = 1
while i < 10:
    j = 1
    while j < 10:
        if i <= j:
            print i * j,
        j = j + 1
    i = i + 1
    print " "









