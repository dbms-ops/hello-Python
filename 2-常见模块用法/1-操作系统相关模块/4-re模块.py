# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

# re 模块：主要用于进行正则表达式匹配
# 正则表达式参考：https://www.runoob.com/regexp/regexp-tutorial.html ；
#

import re


def re_match_help():
    # re.match(pattern,string, flags=0):
    #   patter: 表示进行匹配的正则表达式模式；
    #   string：表示需要进行匹配的字符串；
    #   flags：表示匹配的标志信息,用于控制正则表达式的匹配方式
    #       re.I: 表示忽略大小写
    #       re.L: 进行本地化识别，很少使用；
    #       re.M：进行多行匹配，影响 ^ 和 $ 的行为；
    #       re.S: 使用 . 匹配包括换行符在内的所有字符；
    #       re.U: 根据Unicode字符集解析字符；
    #       re.X: 使用更加灵活的方式来理解正则表达式；；
    #   如果匹配到返回一个match实例对象，否则返回None,math只匹配string的开头
    #   ;
    a = 'abcdefg'
    print re.match(r'abc', a)
    print re.match(r'abc', a).group()
    # 对于匹配失败的返回NULL
    print re.match(r'cba', a)


def re_search_help():
    # re.search(pattern, string, flags=0):
    #   用于查找整个字符串中可以匹配到子串，找到返回对应的实例，否则返回NULL;
    #   pattern: 表示进行匹配的正则表达式模式；
    #   string: 表示需要进行匹配的字符串；
    #   flags: 同 re.match;

    a = 'abcde123fg'
    print re.search(r'bc', a)
    print re.search(r'bc', a).group()
    print re.search(r'123', a)


def re_sub_help():
    # sub：用于进行替换，并且返回替换的次数
    a = 'a1b2c3'
    print re.sub(r'\d+', '0', a), type(re.sub(r'\d+', '0', a))  # 在a里面把数字替换成为0


def re_split_help():
    # re.split(pattern, string, maxsplit=0, flags=0):
    #   pattern: 表示进行匹配的正则表达式模式；
    #   string:表示需要进行匹配的字符串;
    #   maxsplit:
    #   flags: 同re.match;
    #
    # 用pattern匹配的子串来分割string，如果pattern里使用了圆括号，那么被pattern匹配到的串也将作为返回值列表的一部分,
    # maxsplit为最多被分割的字符串个数
    a = 'a4b5c7'
    print re.split(r'\d', a)
    print re.split(r'(\d)', a)


def re_findall_help():
    # re.findall(pattern, string, maxsplit=0, flags=0):
    # 通过列表的方式返回string里面pattern匹配的子串;
    # pattern: 表示进行匹配的正则表达式模式；
    # string: 表示需要进行匹配的字符串；
    # flags: 同 re.match;;
    a = "das12das3cds4fds5fadas22fs6"
    print re.findall(r'\d', a)
    print re.findall(r'\d{2,}', a)


def re_match_project_help():
    # match 对象
    # re.match()、re.search()成功匹配的话都会返回一个Match对象，它包含了关于此次匹配的信息，可以使用Match提供的属性或方法来获取这些信息
    # (?P<sign>.*) 这个没有看懂

    m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
    print "m.string:", m.string
    print "m.re:", m.re
    print "m.pos:", m.pos
    print "m.endpos:", m.endpos
    print "m.lastindex:", m.lastindex
    print "m.lastgroup:", m.lastgroup
    print "m.group(1,2):", m.group(1, 2)
    print "m.groups():", m.groups()
    print "m.groupdict():", m.groupdict()
    print "m.start(2):", m.start(2)
    print "m.end(2):", m.end(2)
    print "m.span(2):", m.span(2)
    print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')


def re_complie_help():
    # Pattern对象
    # 通过re.complie()生成Pattern对象
    pa = re.compile("(\d)")
    print pa.split("he has 2 books and 1 pen")
    print pa.findall("he has 2 books and 1 pen")
    print pa.sub('much', 'he has 2 books and 1 pen')


def re_partern_help():
    # 匹配模式
    # 匹配模式取值可以使用按位或运算符'|'表示同时生效
    # 常见的匹配模式
    # re.IGNORECASE 表示忽略大小写
    pa = re.compile('abc', re.IGNORECASE)
    print pa.findall("AbCdefg")

    # re.LOCALE：表示字符集本地化

    # re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为
    # 这种方式只对于第一行的模式进行匹配
    pa = re.compile("^\d+")
    print pa.findall("123 456\n789 012\n345 678")

    # 改变模式对于多行进行匹配
    pa_m = re.compile("^\d+", re.MULTILINE)
    print pa_m.findall('123 456\n789 012\n345 678')

    # re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为,点号就能匹配包括换行符的任何字符
    pa = re.compile('.+')
    print pa.findall('das\nda\naddw\nsdaq\n')

    pa_d = re.compile('.+', re.DOTALL)
    print pa_d.findall('das\nda\naddw\nsdaq\n')


def re_test_help():
    text = "ip = 127.0.0.1"
    print re.split(r'=', text, maxsplit=2)



# next name
def main():
    re_test_help()


if __name__ == '__main__':
    main()
