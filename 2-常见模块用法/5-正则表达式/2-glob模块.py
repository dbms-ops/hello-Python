#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-23 22:43 
# user: linux
# description: glob 模块用于实现正则表达式的匹配，实现全局的模糊查找,
#
import glob
import os


def find_file(file_path='/etc/snmp/'):
    if os.path.exists(file_path):
        os.chdir(file_path)
        for file_needs in glob.glob(''):
            print os.path.join(file_path, file_needs)
    else:
        print "path: {} is not exists".format(file_path)


def find_file(file_path):
    if os.path.exists(file_path):
        os.chdir(file_path)
        for file_needs in glob.iglob(''):
            print os.path.join(file_path, file_needs)
    else:
        print "path: {} is not exists".format(file_path)


def main():
    find_file()


if __name__ == "__main__":
    main()
