# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
#
# json 模块: 主要是用来进行编码和解码的，;
#
import json
import os


# dumps:用于将 Python 中的字典转换成为字符串；
# loads：用于将字符串转换成为字典；
# dump：用于将数据写入到json文件中；
# load：用于打开 json 文件，并且把字符串变成整数类型；


# dump 用于将数据 dump 为json格式, 并且将数据进行排序;
#   sort_keys: 按照键值对的键进行排序；
#   indent：指定缩进的空白字符；
#   separators：用于指定字符的分隔符号；

# load：用于打开 json 文件，并且把字符串变成整数类型；
def json_read(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as fread:
            return json.load(fread)
    return False


#  dump: 用于将json 格式的文件写入到 filename 中
def json_write(filename, msg):
    """
    :param filename: The name of file which one to write
    :param msg: The message you need to write in filename
    :return: Reture True while write msg to file, Otherwise return False
    """
    if os.path.exists(filename) and len(msg) != 0:
        with open(filename, 'w+') as fwrite:
            json.dump(msg, fwrite, indent=2, sort_keys=True, separators=(',', ': '), encoding='utf-8')
    return False


# dumps:用于将 Python 中的字典转换成为字符串；
def json_dumps(msg):
    if len(msg) != 0:
        return json.dumps(msg, indent=2, separators=(',', ': '), encoding='utf-8')
    return False


# 用于将字符串转换成为字典
def json_loads(msg):
    if len(msg) != 0:
        return json.loads(msg)
    return False


def main():
    student = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
    result = json_dumps(msg=student)
    print type(result)
    print json_loads(result)


if __name__ == '__main__':
    main()
