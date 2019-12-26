# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7

# 递归：
#   函数调用自己本身，就是递归调用；
#   调用自身的函数就是递归函数
#   循环能够解决的事情，递归一定可以解决
#   递归解决方式：
#       1、写出临界条件
#       2、寻找第一次递归和下一次递归的关系
#       3、假设函数功能完善，调用自身的结果以及上一次的结果，计算本次的结果；
#       4、
#
#       ;

# 简单的递归
# 计算n 的 加法

def sumn(n):
    if n == 1:
        return 1
    else:
        return n + sumn(n-1)

print sumn(10)

# 数据结构-栈
# 使用Python现有的数据结构实现栈
# 先进后出的特点
#

list_stack = []

# 向模拟栈里面写入数据

list_stack.append("a")
print list_stack

list_stack.append('b')
print list_stack

list_stack.append('c')
print list_stack

list_stack.append('e')
print list_stack

# 出栈
result = list_stack.pop()
print result

result = list_stack.pop()
print result

# 队列
#   先进先出的数据结构
#
print "queue start: "
import collections

queue = collections.deque()


# 队列写入数据

queue.append('a')
queue.append('b')
queue.append('c')
queue.append('e')
queue.append('f')

# 出队
result = queue.popleft()
print result

result = queue.popleft()
print result







if __name__ == '__main__':
    pass
    