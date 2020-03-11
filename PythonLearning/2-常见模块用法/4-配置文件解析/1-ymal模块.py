# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# yaml 模块：同样是一个用来记录配置文件的模块，功能类似于ConfigParser模块，Yaml也是配置文件的一种记录格式
# 
import os

import yaml


def open_yaml(file):
    if os.path.exists(file):
        with open(file,'rw') as config:
            content = yaml.load(config,Loader=yaml.FullLoader)
            print type(content)
            print "before change: ", content
            content['age'] = 23
            content['name'] = 'linux'
            print "after change: ", content
            yaml.dump(content,config)

def main():
    open_yaml("/tmp/config/config.yaml")


if __name__ == '__main__':
    main()
