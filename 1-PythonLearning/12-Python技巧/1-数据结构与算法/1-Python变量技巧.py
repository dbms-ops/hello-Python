#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-26 22:32 
# user: lixun
# filename:
# description: Python cook book 技巧
# 

def multivariate():
    # 包含 N 个元素的元祖或者序列，解压里面的值，复制给多个变量
    # 元祖 赋值给多个变量
    x, y = (1, 2)
    print x, y

    # 列表元祖 多个变量赋值
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, (year, mon, day) = data
    print name
    print shares
    print price
    print year, mon, day

    # 如果变量个数和序列元素的个数不匹配，会产生一个异常
    """
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module> ValueError: need more than 2 values to unpack
    """
    # 解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器
    # noinspection PyByteLiteral
    print
    print
    # noinspection PyByteLiteral
    print "# 解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器"
    s = "Hello"
    a, b, c, d, e = s
    print a
    print b
    print c
    print d
    print e

    # 在解析使用的过程中，必须保证占位变量名在其他地方没有被使用到


def asteriskValueError(a, b, c, *d):
    # 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么 怎样才能从这个可迭代对象中解压出 N 个元素出来
    # 在Python 2.7 中暂时无法使用
    # 通过 Python 的 * 表达式来解决多个多出变量的问题
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    # name, email, *phone_numbers = record
    # print name
    # print email
    # print phone_numbers
    # *li = '1234'
    # print *li
    print a, b, c, d


# def sum(tems):
#     head, *tail = items
#     return head + sum(tail) if tail else head


def main():
    asteriskValueError(1, 2, 3, 1, 2, 3, 4, 5, 6, 7)


if __name__ == "__main__":
    main()
