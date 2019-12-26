# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
#
# 
import os


# 通过递归实现打印所有的文件和目录
def list_all(dpath,sp=" "):
    file_list = os.listdir(dpath)
    sp += " "
    for fileName in file_list:
        # 判断是否是文件或者是目录需要使用绝对路径
        if os.path.isdir(os.path.join(dpath, fileName)):
            print sp + "dir: {}".format(fileName)
            list_all(fileName,sp)
        else:
            print sp + fileName

# 使用栈结构实现listAll()
#

def list_All_Deep(dpath):
    stack = []
    stack.append(dpath)
    while len(stack) != 0:
        dirPath = stack.pop()




if __name__ == '__main__':
    pass
