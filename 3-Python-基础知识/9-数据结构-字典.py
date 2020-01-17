# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020-1-16 16:57
# user: Administrator
# description: dict 的常见操作
#


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


def create_dict_get_help():
    # 定义字典
    student = {'tom': 59, 'jerry': 89, 'alice': 91}

    # 获取元素
    print student['tom']

    # 获取元素，不存在，不进行报错
    print student.get('Bob')


def add_element():
    # 添加元素
    #   不存在 key进行添加
    #   存在 key进行修改
    student = {'tom': 59, 'jerry': 89, 'alice': 91}
    student['dave'] = 78
    student['tom'] = 79
    print student


def delete_element_help():
    # 删除元素
    student = {'tom': 59, 'jerry': 89, 'alice': 91}
    print student.pop('tom')
    print student


def Traversal_element_help():
    # 字典遍历
    #
    student = {'tom': 59, 'jerry': 89, 'alice': 91}
    for key, value in student.items():
        print key, value

    for key, value in enumerate(student):
        print key, value


def main():
    delete_element_help()


if __name__ == '__main__':
    main()
