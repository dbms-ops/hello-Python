# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# author: Lixun
# argparse:
#   用于进行命令行参数解析
#

import argparse

import argparse

# 创建一个参数解析实例
parser = argparse.ArgumentParser()

# 添加参数解析
parser.add_argument("square", help="display a square of a given number",
                    type=int)
parser.add_argument('-v', '--verbose', help='increase output verbosity')

# 开始解析
args = parser.parse_args()
print(args.square ** 2)





if __name__ == '__main__':
    pass
