#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-07 20:49
# user: linux
# description: glob 模块用于实现正则表达式的匹配，实现全局的模糊查找,支持的正则表达式匹配，这里的正则匹配规则和标准的正则表达式不一样；
# 支持的通配符：
#   *：匹配0或多个字符；
#   **：匹配所有文件、目录、子目录和子目录里的文件 3.5版本新增；
#   ?：匹配1个字符，与正则表达式里的?不同；
#   [exp]：匹配指定范围内的字符，如：[1-9]匹配1至9范围内的字符；
#   [!exp]：匹配不在指定范围内的字符；
# 脚本默认是通过os.chdir()当前目录查找；


import glob
import os


def find_glob(file_path='/etc/snmp/'):
    if os.path.exists(file_path):
        os.chdir(file_path)
        for file_needs in glob.glob(''):
            print os.path.join(file_path, file_needs)
    else:
        print "path: {} is not exists".format(file_path)


def find_iglob(file_path):
    if os.path.exists(file_path):
        os.chdir(file_path)
        for file_needs in glob.iglob(''):
            print os.path.join(file_path, file_needs)
    else:
        print "path: {} is not exists".format(file_path)


def fileCount(filePath):
    if not os.path.exists(filePath):
        os.mkdir(filePath)
    for mongoShakeConf in glob.glob1("/data/mongo-shake", pattern="mongo-shake-[1]"):
        print mongoShakeConf

def main():
    fileCount(filePath="/data/mongo-shake")


if __name__ == "__main__":
    main()
