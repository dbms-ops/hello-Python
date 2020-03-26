#!/data1/Python2.7/bin/python27
# -*-coding:utf-8-*-
# time: 2020-01-24 10:21
# user: linux
# description: 数据结构：简单的字符串
#

# 字符串的四种表现方式

# 只支持单行输出
str1 = "text"
print str1

str1 = 'test'
print str1
print

# 字符串表示：支持多行输出
str1 = """test 
text """
print str1

print
# 对于引号的匹配规则就是尽快的找到匹配的引号，使用不当会导致语法错误
#

str1 = '''text 
test'''
print str1

str1 = "tom say: \"Hi json\""
print str1

st = "tom say: 'Hi json'"
print st

st = 'tom say: \'Hi json\''
print st

# i = 1
# while i < 100:
#     print str(i) + '\b'
#     i = i + 1

# 获取字符串长度
hello = "hello, how are you "
print len(hello)

# 字符串乘法
print hello * 2

# 字符串加法
name = "tom"
print hello + name

# 子串
s1 = "ccaaaaccsse"
s2 = "cc"
print s2 in s1, s1 in s2

# 字符串比较
s1 = "aabb"
s2 = "bbcc"

print s1 < s2, s1 > s2, s1 == s2, len(s1)

# 字符串的访问
# index，slice
# index

s = "abcdefghiqdsaowflaksdsiwqo"
# 对于字符串默认就是一个字符串数组，从0开始计数

print s, "index: ", s[0], s[1], s[-1]

# 字符串索引
print s[1] + s[2] + s[5] + s[9]

# 字符串切片
print s[3:9], s[3:-1], s[:11], s[:len(s)], s[:]

#



# 判断子串以及位置
send = "how,hello,how, are you,how"
sub = "how"

index = 0
print len(send)
# 下标的范围一定需要谨慎，容易越界，也容易没有找到结尾
while index < len(send) - len(sub) + 1:
    if send[index:index + len(sub)] == sub:
        print index, "is here"
    index += 1
    # print index


# 删除字符串里面的指定的子串
#
send = "hello,xx You are my frxixxexnd XXxx"
sub = "xx"
index = 0
while index < len(send) - len(sub) + 1:
    if send[index:index + len(sub)] == sub:
        send = send[:index] + send[index + len(sub):]
    else:
        index += 1
print send, "is here..."



# chr函数：用于将整型转换成为字符

x = 97
i = 0
while i < 26:
    a = str(i)
    print a, chr(i+x),
    i += 1

# ord:用于将字符转换成为整型
send = "hello,man, what is weather today"
index = 0
while index < len(send):
    print send[index],ord(send[index]),
    index += 1


























