#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/19 16:48
# @user: Administrator
# @fileName: 16-tarfile模块.py
# @description: tarfile 模块 用于进行文档归档
# 
import os
import tarfile


def creatTarfile():
    tmpTar = tarfile.open("/data/backup/1.tar.gz", "w:gz")
    for root, dir, files in os.walk("/data/backup"):
        for file in files:
            fullPath = os.path.join(root, file)
            tmpTar.add(fullPath)
    tmpTar.close()


def extra(tarPath, targetPath):
    try:
        tar = tarfile.open(tarPath, "r:gz")
        fileNames = tar.getnames()
        for fileName in fileNames:
            tar.extract(fileName, targetPath)
        tar.close()
    except Exception as e:
        print e


def main():
    extra("/data/backup/1.tar.gz", "/data/backup")


if __name__ == '__main__':
    main()
