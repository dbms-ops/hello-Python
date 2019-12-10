# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
# author: Lixun

# string模块：用于进行常见的字符串处理
import string

# 字符串中首字母转换成为大写
s = "the quick brown fox jumped over the lazy dog."
print s
print string.capitalize(s)
print s.capitalize()

# 使用空格填充字符长度为width，并且将原字符居中
s = "The quick brown fox jumped over the lazy dog."
print s.center(100)

# 用于返回字符串sub在S中出现的次数
s = "The quick brown fox ro juromped over the lazy dog."
sub = "ro"
print s.count(sub)

# 以指定的格式编解码码字符串
print s.encode("utf-8").decode("utf-8")

# 判断字符串是否以 S 结尾
s = "The quick brown fox ro juromped over the lazy dog."
print s.endswith("dog.")

# 查找字符串在目标串中的位置,没有返回-1
s = "The quick brown fox ro juromped over the lazy dog."
sub = "ro"
print s.find(sub)

# 用于进行字符转换
# 首先需要定义字符转换规则
leet = string.maketrans('abegiloprstz', '463611092572')
s = "The quick brown fox jumped over the lazy dog."
print s
print string.translate(s,leet)

#