# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7


# 数据结构-元组
#       元组：元组和列表类似，但是元组内的元素是不可变得
#


# 定义元素
number = (1, 2, 3, 4, 5, 6,[1,2,3,4])
print type(number), number

# 获取元组元素
print number[0], number[1], number[2], number[-3]

# 元组里面的元素是不允许进行修改的
number[6][1] = "name"
print number

# 清空并且删除元组
del number

# 元组的操作
# 元组相加

num = (1,2,3,4,5)
name = ('alice','tom','jerry')
print num + name

# 元组重复
print num * 3

# 元组包含
print 11 in num

# 元组截取
num = (1,2,3,4,5,6,7,8,9) * 3
print num
print num[0:-1]
print num[4:-4]

# 二维元组
num = ((1,2,3),(4,5,6),(7,8,9))
print num

# 元组的方法
# 元组中元素的个数
len(num)

# 元组中的最大值
print max(num)

# 元组中的最小值
print min(num)

# 列表转换元组
num = tuple(list(num))
print num

# 元组循环
for i in num:
    for j in i:
        print j

#




if __name__ == '__main__':
    pass
    