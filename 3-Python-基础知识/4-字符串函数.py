# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

#
# 总结常见字符串函数
#
# eval(): 将字符串当作一个表达式计算结果
print eval("123"), eval("+112"), eval("-123"), eval("123/12")

# len(): 用于返回字符串的长度
print len("A good beginning is half done")

# lower(): 转转字符串中的大写为小写
str1 = "A GOOD BEGINNING IS HALF DONE"
print str1.lower()

# upper():转换小写为大小
print str1.lower().upper()

# swapCase(): 将字符串中的大写转换成为小写，将小写转换成为大写
str2 = "A gOOd beGiNiNg iS HalF DonE"
print str2.swapcase()

# capitalize(): 保持首字母大写，其他的都是小写
str2 = " A gOOd beGiNiNg iS HalF DonE "
print str2.capitalize()

# title(): 每个单词的首字母大写
print str2.title()

# center(width,fillChar): 填充字符到一定的长度
print str2.center(44, '=')

# lJust(width,fillChar): 用于进行左对齐
print str2.ljust(44, "-")

# rJust(width,fillChar): 用于进行右对齐
print str2.rjust(44, '=')

# zfill(width): 返回一个长度为width的 字符串，右对齐，填充0
print str2.zfill(34)

# count(str[,start][,end]): 返回str出现的次数
print str2.count("gOOd", 3)

# find(str[,start][,end]): 用于查找某个字符串,返回的是第一次查找到的下标,否则返回-1
print str2.find("gOOd")

# rfind(str[,start][,end]): 用于从右向左进行查找
print str2.rfind("gOOd")

# index(str,start=0,end=len(str)):查找原则和 find 一样，但是如果不存在抛出异常
try:
    print str2.index("Good")
except:
    print "There is a abnormal"

# rIndex(str,start=0,end=len(str)):查找原则和 find 一样，但是如果不存在抛出异常
try:
    print str2.rindex("Good")
except:
    print "There is a abnormal"

# ltrip(char): 删除字符串开始左边指定的字符
str2 = "00000000A gOOd beGiNiNg iS HalF DonE"
print str2.lstrip("0")

# rtrip(char): 删除字符串开始右边指定的字符
str2 = "00000000A gOOd beGiNiNg iS HalF DonE000000000"
print str2.lstrip("0")

# strip()：删除掉字符串左边或者右边的某些字符
str2 = "00000000A gOOd beGiNiNg iS HalF DonE000000000"
print str2.strip("0")

# ord()：查找字符的ASCII值
print ord('A'), ord('B')

# chr(): 用于将ASCII转换成为对应的字符
print chr(97), chr(89)

# 字符串大小比较：从首字符开始依次进行比较，如果相等比较下一个ASCII字符的大小
print "aaaaa" < "bbbbb", "aa" > "caa"

# split(str[,num]): 字符串分割
#   str:表示按照str进行字符串切割
#   num：表示仅仅截取num指定的个数，剩下的不在进行截取
#
proverb = "Faith wi ll mo v e mountains"
print proverb.split(" ", 3)

# splitlines():
#   按照('\r','\n','\r\n') 进行分割，返回一个列表

proverb = """
Time flies like an arrow
Where there is smoke, there is fire.
The pot calls the kettle black.
Monkey see, monkey do.
Not getting what you want is sometimes a wonderful stroke of luck. 
"""
print proverb.strip().splitlines()

# join(str):用于将字符串组合成为一个字符串
print '\n\r'.join(proverb.strip().splitlines())

# 字符串中的最大值与最小值
print max(proverb), '**{}**'.format(min(proverb))

# 字符串替换

# replace(oldStr, newStr, count):
#   使用newStr替换oldStr，并且可以指定替换的次数
print proverb.replace("like", 'not like', 1)

import string

# 字符串映射表
# 这里的映射是按照单个字符进行映射的
temp = string.maketrans('good', 'nice')
print proverb.translate(temp)

# startswith(prefix[, start[, end]]):
#    判断字符是否以某个字符换开头
print proverb.startswith('Time', 1, len(proverb))

# endswith(prefix[, start[, end]]):
#   判断字符串是否是以某个字符串结尾的
#

print proverb.endswith('time', 1, len(proverb))

# encode(encoding='utf-8',errors='strict')
#   用于进行数据编码，默认是'utf-8'

proverb = "One generation plants the trees, another gets the shade."
proverbUtf = proverb.encode('utf-8')
print proverbUtf, type(proverbUtf)

# decode(): 用于进行字符串解码c操作
print proverbUtf.decode('utf-8'), type(proverbUtf.decode('utf-8'))

# 编码需要和解码一致

# isalpha():
#   至少有一个字符，并且字符都是字母
print proverbUtf.isalpha()

# isalnum():
#   至至少有一个字符，且所有字符都是字母或者是数字
print proverbUtf.isalnum()

# isupper():
#   至少有一个英文字符，并且所有的字符都是大写
print 'ABC'.isupper()
print 'ABC1'.isupper()
print '1'.isupper()
print 'ABC#'.isupper()

# islower():
#   至少有一个英文字符，并且所有的字符都是小写
print 'abc'.islower()
print 'abc1'.islower()
print '1'.islower()
print 'abc#'.lower()

# istitle():
#   如果字符串是标题化的[首字母大写]，返回为True
print 'One Generation'.istitle()

# isdigit():
#   如果字符串只包含数字字符，返回True，否则返回False
print '123'.isdigit()
print '123a'.isdigit()
# isnumeric(): 同上，但是2.7不支持
#

# 2.7 不支持： isdecimal(): 字符串只包含十进制字符，为True，否则为False
# isspace():
#   如果字符串只包含空格，返回True
print '123'.isspace()
print '\n'.isspace()
print '\t'.isspace()
print ' '.isspace()
print '\r'.isspace()








if __name__ == '__main__':
    pass
