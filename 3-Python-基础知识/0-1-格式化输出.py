# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7

# 格式化输出 print 使用
#
#
# 输出整数，字符串，浮点数
num = 10
numFloat = 10.111213
proverb2 = "Love is a carefully designed lie"
print "num = ", 6
print "num = %d \n %s" % (num, proverb2)
print "str = %s \n %.3f" % (proverb2, numFloat)

# 输出多行
#
print '''
In the eyes of the lover, the one thousand mile journey but a mile
As long as I think of you, dear friend, all losses are restored and sorrows end
Why I have never catched the happiness whenever I want you, I will be accompanyed by the memory.
When you need to tell, I am here; when you need a warm hug, I will be here; when you need someone to wipe your tears of
 sadness, I will here.
'''

# 字符串转义
#   \t：表示制表符
#   \n：表示换行符
#   \r:
#   r: 表示里面的内容不进行转义
print r'\\\t\\t\\\t', '\\\t\\t\\\t'

#

if __name__ == '__main__':
    pass

import logging


