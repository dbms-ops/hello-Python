# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
#
#
# sorted 函數：
#
#

# 升序排序
print sorted([1,5,4,2,3,6,7,8,0])

# 按照绝对值进行排序
# key 接受函数，用来实现自定义排序规则
print sorted([-1,-3,3,5,-9,0,11],key=abs)

# 降序排序
print sorted([-1,-3,3,5,-9,0,11],reverse=True)

# 按照字符串的长短进行排序
print sorted(['1112','1121121','11','123','123456'],key=len)




if __name__ == '__main__':
    pass