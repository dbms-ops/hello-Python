# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
# author: linux
# 数据结构-列表：
#   Python中简单的数据结构
#   列表：列表是一个有序的集合，
# 创建列表
# 列表中的元素类型是不进行限制的
address = ['GZ','HK','XA','BJ','SH',1,2,3,['Shanghai','Beijing'],(1,2,3)]

# 从列表中取值
print  address[0]

# 替换列表中的值，列表中的值是可以替换的，但是元组是不可以替换的
address[0] = ["name",'address']
print address[0:-1]

# 对于列表的下标访问是不可以越界的

# 列表操作
# 列表组合: 在不修改原来列表的基础上形成一个新的列表
#
print address + address

# 列表的重复
print address * 2

# 判断元素是否在列表中
print 1 in address,'HK' in address,'changJiang' in address

# 列表截取
print address[0:3],address[0:-1]

# 多维列表
name = [['Dove','Channel'],'Jack Ma','Tom','Jerry',['Shanxi','Jerry']]
print name[0][1]

# 列表方法
#   添加元素:当做一个元素追加
name.append('Tom')
name.append(['12','23','34'])
#   把一个列表中的值追加到当前列表中
name.extend([1,2,3])

#   插入元素到任意的位置
num = [1,2,3,4,5]
num.insert(3,23)
num.insert(2,['name','apple'])
print num

# 删除指定位置的元素，默认最后一个元素的下标，并且返回删除的数据
num.pop()
num.pop(2)

# 移除指定的元素,默认只移除第一个匹配的结果元素
num.remove(4)

# 清除列表中的所有数据,2.7 没有clear
# num.clear()

# 查找元素的下标,匹配第一个元素的索引值
num.extend([13,4,22,42,1,345,53,2,3])
print num.index(23,3,7)

# 元素个数计数
print len(num)

# 获取列表中的最大值
print max(num)

# 获取列表中的最小值
print min(num)

#



if __name__ == '__main__':
    pass
    