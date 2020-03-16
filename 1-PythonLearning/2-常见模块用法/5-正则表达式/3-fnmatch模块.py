#
# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
# time: 2020-01-24 10:21 
# user: linux
# description: fnmatch 模块用于实现
# 支持的通配符：
#   *：匹配0或多个字符；
#   **：匹配所有文件、目录、子目录和子目录里的文件 3.5版本新增；
#   ?：匹配1个字符，与正则表达式里的?不同；
#   [exp]：匹配指定范围内的字符，如：[1-9]匹配1至9范围内的字符；
#   [!exp]：匹配不在指定范围内的字符；


import fnmatch
import os


def fnmatch_fnmatch(file_path, pattern):
    """
    Patterns are Unix shell style:

    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

    An initial period in FILENAME is not special.
    Both FILENAME and PATTERN are first case-normalized
    if the operating system requires it.
    If you don't want this, use fnmatchcase(FILENAME, PATTERN).
    :param file_path:
    :param pattern:
    :return:
    """
    for file_name in os.listdir(file_path):
        result = fnmatch.fnmatch(file_name, pattern)
        print result


def fnmatch_filter(file_path, file_pattern):
    """
    Return the subset of the list NAMES that match PAT
    :param file_path:
    :param file_pattern:
    :return:
    """
    for file_name in os.listdir(file_path):
        return fnmatch.filter(file_name, file_pattern)




def main():
    print fnmatch_fnmatch('/tmp/', 'pycharm_*')


if __name__ == "__main__":
    main()
