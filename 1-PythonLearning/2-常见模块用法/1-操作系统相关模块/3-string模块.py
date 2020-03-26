#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/19 16:48
# @user: Administrator
# @fileName: strings模块.py
# @description: string 字符串的相关方法
#


# string模块：用于进行常见的字符串处理
import string


def InitialCapital():
    # 字符串中首字母转换成为大写
    s = "the quick brown fox jumped over the lazy dog."
    print s
    print string.capitalize(s)
    print s.capitalize()


def stringCenter():
    # 使用空格填充字符长度为width，并且将原字符居中
    s = "The quick brown fox jumped over the lazy dog."
    print s.center(100)


def countSubstring():
    # 用于返回字符串sub在S中出现的次数
    s = "The quick brown fox ro juromped over the lazy dog."
    sub = "ro"
    print s.count(sub)


def stringEncode():
    # 以指定的格式编解码码字符串
    print s.encode("utf-8").decode("utf-8")


def stringEndWith():
    # 判断字符串是否以 S 结尾
    s = "The quick brown fox ro juromped over the lazy dog."
    print s.endswith("dog.")


def stringFindPosition():
    # 查找字符串在目标串中的位置,没有返回-1
    s = "The quick brown fox ro juromped over the lazy dog."
    sub = "ro"
    print s.find(sub)


# index(s):用于查找字符串，如果不存在返回异常
def stringIndex():
    s = "The quick brown fox ro juromped over the lazy dog."
    sub = "roo"
    try:
        print s.index(sub)
    except:
        print "throw error"


# True：至少有一个字符并且都是字母或者数字
def stringIsnalnum():
    s = "The quick brown fox ro juromp1ed over the lazy dog."
    s1 = ""
    print s.isalnum(), s1.isalnum()


def stringIsalpha():
    # True:至少存在一个字符，并且都是字母
    s = "The quick br4ow2n1 fo3x ro ju5romp1ed o3ver th4e lazy dog."
    s1 = "Thequick"
    print s.isalpha(), s1.isalpha()


def stringIsdigit():
    # True: 只包含数字
    s = "111111 223"
    s1 = "11111"
    print s.isdigit(), s1.isdigit()


def stringIsspace():
    # True: 只包含空格
    s = "    "
    s1 = " 1 2 3"
    print s.isspace(), s1.isspace()


def
# ljust():左对齐，使用空格从左边开始填充
s = "                        Actions speak louder than words"
print s.ljust(56)

# .lstrip():去掉左边开始的不可见字符
s = "                        Actions speak louder than words"
print s.lstrip()

# S.partition(s):用 S 将 str 切分成为三个值
sf = "From small beginnings comes great things"
ss = "small"
print sf.partition(ss)

# lower():用于将大写转换称为小写
s = "Every man is his own worst enemy"
print s.lower()

# a.replace(b): 使用 b 替换 a 里面的字符串
s = "The voice of one man is the voice of no one"
sub = "two"
print s.replace("one", sub)

# str.rfind():用于从右边开始进行查找
s = "The voice of one man is the voice of no one"
sub = "one"
print s.rfind(sub), s.find(sub)

# str.rindex():类似于index，从右边开始查找
s = "The voice of one man is the voice of no one"
sub = "one"
print s.index(sub), s.rindex(sub)

# str.rjust():返回一个右对齐的，使用空格填充至长度为width的新字符串
s = "The voice of one man is the voice of no one"
print s.rjust(56)

# str.rpartition(s): 类似于partition，从右边开始查找
sf = "From small beginnings comes small great things"
ss = "small"
print sf.rpartition(ss)

# r.strip():去掉右边的不可见字符
s = "    Actions speak louder than words             "
print s.rstrip()

# s.split(s):以s为分隔符号进行切片
s = "A great ship asks for deep waters Two heads are better than one " * 4
print s.split("A")[0]
print s.split("are")[2]
print type(s.split("A"))

# s.splitlines(): 按照行进行分割，返回一个包含各行元素的列表，用于处理文件比较常见

# s.startwith(s):判断字符串S是否是按照s开头的
s = "A great ship asks for deep waters Two heads are better than one " * 4
print s.startswith("A"), s.startswith("G")

# s.strip():相当于同时执行 lstrip(), rstrip()

s = "                        Actions speak louder than words                   "
print s.lstrip()

# s.title():返回所有单次首字母大写的，其余为小写
s = "If a thing is worth doing it is worth worth doing well."
print s.title()

# str.upper():返回str所有字符的大写字符串
s = "If a thing is worth doing it is worth worth doing well."
print s.upper()

# str.zfill(width): 返回长度为 width 的字符串，原字符str右对齐，填充 0
s = "If a thing is worth doing it is worth worth doing well."
s.zfill(178)

#

# 用于进行字符转换
# 首先需要定义字符转换规则
leet = string.maketrans('abegiloprstz', '463611092572')
s = "The quick brown fox jumped over the lazy dog."
print s
print string.translate(s, leet)

# 字符串常用技巧
# 字符串反转
str = "123456"
print str, str[::-1]

# 字符串拼接尽量使用join,+需要多次申请内存,按照以下方式拼接字符串
s = "Nothing "
s1 = "great "
s2 = "was "
s3 = "ever "
s4 = "achieved "
s5 = "without "
s6 = "enthusiasm."
print ''.join([s, s1, s2, s3, s4, s5, s6])
print s + s1 + s2 + s3 + s4 + s5 + s6

# 按照固定长度分割字符串
import re

s = "1234567890"
print re.findall(r'.{1,3}', s)

# 优雅的字符串
SQL = ('SELECT COUNT(*) FROM TABLE_NAME '
       'WHER ID = 10 '
       'GROUP BY SEX'
       )
print SQL

# 将print 的字符串写入文件
print >> open("somefile.txt", "w+"), "Hello World"

#
