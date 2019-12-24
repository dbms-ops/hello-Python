# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
# author: Lixun

# 偏函数：
#  利用原有函数的功能，申明类似的函数，实现简单的功能
#
#   ；
print int('10010',base=2)

# 偏函数
def int2(str,base = 2):
    return int(str,base)

print int2("1001001")

# 利用模块生成偏函数
import functools
int_2 = functools.partial(int,base=2)
print int_2('0010001110')

#


if __name__ == '__main__':
    pass
    