# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# properties：该文件主要是java生成的配置文件，通过第三方模块来解析 示例的配置文件
# 自定义的一个类，用于实现解析 properties 格式的配置文件，支持了get，set，两个方法；
# 该模块操作文件时，会覆盖旧版本的文件，所以尽量不要写入注释等信息；

import os

import javaproperties


class Properties(object):
    def __init__(self, filename):
        self.__filename = filename

    def get(self, key):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'r') as fread:
                result = javaproperties.load(fread)
                return result.get(key)
        return False

    def set(self, key, value):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'r') as fread:
                result = javaproperties.load(fread)
                result[key] = value
            os.remove(self.__filename)
            with open(self.__filename, 'w') as fwrite:
                javaproperties.dump(result, fwrite, timestamp=None)
        return False


def main():
    config_read = Properties("/tmp/config/conf.properties")
    config_read.set('data-dir1', '/data1/mysql-db')


if __name__ == '__main__':
    main()
