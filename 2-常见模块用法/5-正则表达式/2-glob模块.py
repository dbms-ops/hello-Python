#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-23 22:43 
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


def main():
    find_glob()



if __name__ == "__main__":
    main()
