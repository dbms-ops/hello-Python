#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020/1/16 16:57
# user: Administrator
# description: 常见的字符串函数
#

#
# 总结常见字符串函数
#


def eval_help():
    # eval(): 将字符串当作一个表达式计算结果
    print eval("123"), eval("+112"), eval("-123"), eval("123/12")


def len_help():
    # len(): 用于返回字符串的长度
    print len("A good beginning is half done")


def lower_help():
    # lower(): 转转字符串中的大写为小写
    str1 = "A GOOD BEGINNING IS HALF DONE"
    print str1.lower()


def upper_help():
    str1 = "A GOOD BEGINNING IS HALF DONE"
    # upper():转换小写为大小
    print str1.lower().upper()


def swap_case_help():
    # swapCase(): 将字符串中的大写转换成为小写，将小写转换成为大写
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.swapcase()


def capitalize_help():
    # capitalize(): 保持首字母大写，其他的都是小写
    str2 = "A gOOd beGiNiNg iS HalF DonE "
    print str2.capitalize()


def title_help():
    # title(): 每个单词的首字母大写
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.title()


def center_help():
    # center(width,fillChar): 填充字符到一定的长度
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.center(44, '=')


def lJust_help():
    # lJust(width,fillChar): 用于进行左对齐
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.ljust(44, "-")


def rJust_help():
    # rJust(width,fillChar): 用于进行右对齐
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.rjust(44, '=')


def zfill_help():
    # zfill(width): 返回一个长度为width的 字符串，右对齐，填充 0
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.zfill(34)


def count_help():
    # count(str[,start][,end]): 返回str出现的次数
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.count("gOOd", 3)


def find_help():
    # find(str[,start][,end]): 用于查找某个字符串,返回的是第一次查找到的下标,否则返回-1
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.find("gOOd")


def rfind_help():
    # rfind(str[,start][,end]): 用于从右向左进行查找
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    print str2.rfind("gOOd")


def index_help():
    # index(str,start=0,end=len(str)):查找原则和 find 一样，但是如果不存在抛出异常
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    try:
        print str2.index("Good")
    except:
        print "There is a abnormal"


def rIndex_help():
    # rIndex(str,start=0,end=len(str)):查找原则和 find 一样，但是如果不存在抛出异常
    str2 = "A gOOd beGiNiNg iS HalF DonE"
    try:
        print str2.rindex("Good")
    except:
        print "There is a abnormal"


def ltrip_help():
    # ltrip(char): 删除字符串开始左边指定的字符
    str2 = "00000000A gOOd beGiNiNg iS HalF DonE"
    print str2.lstrip("0")


def rtrip_help():
    # rtrip(char): 删除字符串开始右边指定的字符
    str2 = "00000000A gOOd beGiNiNg iS HalF DonE000000000"
    print str2.lstrip("0")


def strip_help():
    # strip()：删除掉字符串左边或者右边的某些字符
    str2 = "00000000A gOOd beGiNiNg iS HalF DonE000000000"
    print str2.strip("0")


def ord_help():
    # ord()：查找字符的ASCII值
    print ord('A'), ord('B')


def chr_help():
    # chr(): 用于将ASCII转换成为对应的字符
    print chr(97), chr(89)


def Compare_ASCII():
    # 字符串大小比较：从首字符开始依次进行比较，如果相等比较下一个ASCII字符的大小
    print "aaaaa" < "bbbbb", "aa" > "caa"


def split_help():
    # split(str[,num]): 字符串分割
    #   str:表示按照str进行字符串切割
    #   num：表示仅仅截取num指定的个数，剩下的不在进行截取
    #
    proverb = "Faith wi ll mo v e mountains"
    print proverb.split(" ", 3)


def splitlines_help():
    # splitlines():
    #   按照('\r','\n','\r\n') 进行分割，返回一个列表

    proverb = """
    Time flies like an arrow
    Where there is smoke, there is fire.
    The pot calls the kettle black.
    Monkey see, monkey do.
    Not getting what you want is sometimes a wonderful stroke of luck. 
    """
    print proverb.strip().splitlines()

    # join(str):用于将字符串组合成为一个字符串
    print '\n\r'.join(proverb.strip().splitlines())

    # 字符串中的最大值与最小值
    print max(proverb), '**{}**'.format(min(proverb))


def replace_help():
    # 字符串替换

    # replace(oldStr, newStr, count):
    #   使用newStr替换oldStr，并且可以指定替换的次数
    proverb = """
       Time flies like an arrow
       Where there is smoke, there is fire.
       The pot calls the kettle black.
       Monkey see, monkey do.
       Not getting what you want is sometimes a wonderful stroke of luck. 
       """
    print proverb.replace("like", 'not like', 1)


def String_translate_help():
    import string

    # 字符串映射表
    # 这里的映射是按照单个字符进行映射的
    proverb = """
       Time flies like an arrow
       Where there is smoke, there is fire.
       The pot calls the kettle black.
       Monkey see, monkey do.
       Not getting what you want is sometimes a wonderful stroke of luck. 
       """
    temp = string.maketrans('good', 'nice')
    print proverb.translate(temp)


def startwith_help():
    # startswith(prefix[, start[, end]]):
    #    判断字符是否以某个字符换开头
    proverb = """
       Time flies like an arrow
       Where there is smoke, there is fire.
       The pot calls the kettle black.
       Monkey see, monkey do.
       Not getting what you want is sometimes a wonderful stroke of luck. 
       """
    print proverb.startswith('Time', 1, len(proverb))


def endwith_help():
    # endswith(prefix[, start[, end]]):
    #   判断字符串是否是以某个字符串结尾的
    #
    proverb = """
       Time flies like an arrow
       Where there is smoke, there is fire.
       The pot calls the kettle black.
       Monkey see, monkey do.
       Not getting what you want is sometimes a wonderful stroke of luck. 
       """

    print proverb.endswith('time', 1, len(proverb))


def endoce_help():
    # 对于字符串进行编码和解码操作
    # encode(encoding='utf-8',errors='strict')
    #   用于进行数据编码，默认是'utf-8
    proverb = "One generation plants the trees, another gets the shade."
    proverbUtf = proverb.encode('utf-8')
    print proverbUtf, type(proverbUtf)

    # decode(): 用于进行字符串解码c操作
    # 编码需要和解码一致
    print proverbUtf.decode('utf-8'), type(proverbUtf.decode('utf-8'))


def isalpha_help():
    # isalpha():
    #   至少有一个字符，并且字符都是字母
    proverb = "One generation plants the trees, another gets the shade."
    proverbUtf = proverb.encode('utf-8')
    print proverbUtf.isalpha()


def isnum_help():
    # isalnum():
    #   至至少有一个字符，且所有字符都是字母或者是数字
    proverb = "One generation plants the trees, another gets the shade."
    proverbUtf = proverb.encode('utf-8')
    print proverbUtf.isalnum()


def isupper_help():
    # isupper():
    #   至少有一个英文字符，并且所有的字符都是大写
    print 'ABC'.isupper()
    print 'ABC1'.isupper()
    print '1'.isupper()
    print 'ABC#'.isupper()


def islower_help():
    # islower():
    #   至少有一个英文字符，并且所有的字符都是小写
    print 'abc'.islower()
    print 'abc1'.islower()
    print '1'.islower()
    print 'abc#'.lower()


def istitle_help():
    # istitle():
    #   如果字符串是标题化的[首字母大写]，返回为True
    print 'One Generation'.istitle()


def isdigit_help():
    # isdigit():
    #   如果字符串只包含数字字符，返回True，否则返回False
    print '123'.isdigit()
    print '123a'.isdigit()
    # isnumeric(): 同上，但是2.7不支持


def isspace_help():
    # 2.7 不支持： isdecimal(): 字符串只包含十进制字符，为True，否则为False
    # isspace():
    #   如果字符串只包含空格，返回True
    print '123'.isspace()
    print '\n'.isspace()
    print '\t'.isspace()
    print ' '.isspace()
    print '\r'.isspace()


def string_rtrip_help():
    comment_string = "10.21.34.232"
    print comment_string.rstrip(".34.232")


def string_ltrip_help():
    comment_string = "10.21.34.232"
    print comment_string.lstrip("10.21.")


def main():
    string_ltrip_help()


if __name__ == '__main__':
    main()
