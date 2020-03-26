#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020/1/16 16:57
# user: Administrator
# description: print 格式化输出文本
# 

# 格式化输出 print 使用
#
#
# 输出整数，字符串，浮点数
def printSample():
    num = 10
    numFloat = 10.111213
    proverb2 = "Love is a carefully designed lie"
    print "num = ", 6
    print "num = %d \n %s" % (num, proverb2)
    print "str = %s \n %.3f" % (proverb2, numFloat)


def printMultiLine():
    # 输出多行
    #
    print '''
    In the eyes of the lover, the one thousand mile journey but a mile
    As long as I think of you, dear friend, all losses are restored and sorrows end
    Why I have never catched the happiness whenever I want you, I will be accompanyed by the memory.
    When you need to tell, I am here; when you need a warm hug, I will be here; when you need someone to wipe your tears of
     sadness, I will here.
    '''


def printEscape():
    # 字符串转义
    #   \t：表示制表符
    #   \n：表示换行符
    #   \r:
    #   r: 表示里面的内容不进行转义
    print r'\\\t\\t\\\t', '\\\t\\t\\\t'


def stringFormatLeft():
    matLeft = "{:<30}{:<30}{:<30}{:<30}"
    print matLeft.format("Schema", "Table", "QPS", "TPS")
    print matLeft.format(1, 2, 3, 4)


def stringFormatCenter():
    matCenter = "{:^20}{:^20}{:^20}{:^20}"
    print(matCenter.format("Schema", "Table", "QPS", "TPS"))
    print matCenter.format(1, 2, 3, 4)


def stringFormatRight():
    matRight = "{:>20}\t{:>28}\t{:>32}\t{:>36}"
    print(matRight.format("Schema", "Table", "QPS", "TPS"))
    print matRight.format(1, 2, 3, 4)

def main():
    stringFormatLeft()



if __name__ == '__main__':
    main()
