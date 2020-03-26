# !/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: list 的常见操作
#


def create_list():
    # 数据结构-列表：
    #   Python中简单的数据结构
    #   列表：列表是一个有序的集合，
    # 创建列表
    # 列表中的元素类型是不进行限制的
    """

    :return: return None
    """
    address = ['GZ', 'HK', 'XA', 'BJ', 'SH', 1, 2, 3, ['Shanghai', 'Beijing'], (1, 2, 3)]

    # 从列表中取值
    print address[0]

    # 替换列表中的值，列表中的值是可以替换的，但是元组是不可以替换的
    # 对于列表的下标访问是不可以越界的
    address[0] = ["name", 'address']
    print address[0:-1]


def list_function():
    # 列表操作
    # 列表组合: 在不修改原来列表的基础上形成一个新的列表
    #
    address = ['GZ', 'HK', 'XA', 'BJ', 'SH', 1, 2, 3, ['Shanghai', 'Beijing'], (1, 2, 3)]
    print address + address

    # 列表的重复
    print address * 2

    # 判断元素是否在列表中
    print 1 in address, 'HK' in address, 'changJiang' in address

    # 列表截取
    print address[0:3], address[0:-1]


def Multidimensional_list():
    # 多维列表
    name = [['Dove', 'Channel'], 'Jack Ma', 'Tom', 'Jerry', ['Shanxi', 'Jerry']]
    print name[0][1]


def append_help():
    name = [['Dove', 'Channel'], 'Jack Ma', 'Tom', 'Jerry', ['Shanxi', 'Jerry']]
    # 列表方法
    #   添加元素:当做一个元素追加
    name.append('Tom')
    name.append(['12', '23', '34'])
    #   把一个列表中的值追加到当前列表中
    name.extend([1, 2, 3])


def index_insert_help():
    #   插入元素到任意的位置
    num = [1, 2, 3, 4, 5]
    num.insert(3, 23)
    num.insert(2, ['name', 'apple'])
    print num

    # 删除指定位置的元素，默认最后一个元素的下标，并且返回删除的数据
    num.pop()
    num.pop(2)

    # 移除指定的元素,默认只移除第一个匹配的结果元素
    num.remove(4)

    # 清除列表中的所有数据,2.7 没有clear
    # num.clear()

    # 查找元素的下标,匹配第一个元素的索引值
    num.extend([13, 4, 22, 42, 1, 345, 53, 2, 3])
    print num.index(23, 3, 7)


def len_list():
    # 元素个数计数
    num = [1, 2, 3, 4, 5]
    print len(num)


def max_list():
    # 获取列表中的最大值
    num = [1, 2, 3, 4, 5]
    print max(num)


def min_list():
    # 获取列表中的最小值
    num = [1, 2, 3, 4, 5]
    print min(num)


def count_list():
    # 统计某个元素出现的个数
    num = [1, 2, 3, 4, 5]
    print num.count(4)


def reverse_help():
    # 列表反转
    num = [1, 2, 3, 4, 5]
    print num
    num.reverse()
    print num


def sort_help():
    # 排序
    num = [1, 2, 3, 4, 5]
    num.sort()
    print num


def copy_help():
    # 拷贝
    #   浅拷贝：引用拷贝，类似于软链接，引用的地址是一样的
    num = [1, 2, 3, 4, 5]
    print num
    numCpoy = num
    num[3] = 'change it'
    print id(num), num
    print id(numCpoy), numCpoy


#   深拷贝：内存拷贝，引用的地址是不一样的
# Python 2.7 不支持深拷贝
# numCpoyNew = num.copy()

def element_conversie_list():
    # 元组转成列表
    mail = ('linux@163.com', 'linux@qq.com', 'linux@yy.com', 'linux@qq.com', 'linux@gmail.com')
    print list(mail)

    result = list(mail)
    result.reverse()
    print result


def main():
    element_conversie_list()


if __name__ == '__main__':
    main()
