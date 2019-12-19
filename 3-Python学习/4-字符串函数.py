# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# author: Lixun
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
print "aaaaa" < "bbbbb","aa" > "caa"




if __name__ == '__main__':
    pass
