# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7


# 字典：
#   使用 key-value 存储，具有极快的查询速度
#   key：
#       1、必须唯一
#       2、key必须是不可变得对象，字符串、整数、list[不可以]
#
#   value:
#       1、
#   1、字典是无序的
#   2、

# 对比list：
#   1、查找和插入的速度很快，不会随着key和value的增加变慢
#   2、占据的内存较大


# 定义字典
student = {'tom':59,'jerry':89,'alice':91}

# 获取元素
print student['tom']

# 获取元素，不存在，不进行报错
print student.get('Bob')

# 添加元素
#   不存在 key进行添加
#   存在 key进行修改
student['dave'] = 78
student['tom'] = 79
print student

# 删除元素
print student.pop('tom')
print student

# 字典遍历
#
for key, value in student.items():
    print key,value

for key, value in enumerate(student):
    print key, value


# 字典的用法之一：
#
property = '''
One generation plants the trees, another gets the shade.
A word once spoken can never be recalled.
Beauty is in the eye of the beholder.
Every dog has his day.
A miss is as good as a mile.
'''




if __name__ == '__main__':
    pass
    