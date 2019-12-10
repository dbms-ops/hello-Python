# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python27
#

import os

# print "获取当前脚本工作的目录路径: "
print os.getcwd()

# "修改当前目录为path"
os.chdir("/root/script/tmp/")
print os.getcwd()

# 执行操作系统命令
os.system("ls")
print os.getcwd()

# 创建目录:用于创建单层级别目录
# 不传递 mode 关键字
if not os.path.exists("temp"):
    os.mkdir("temp", 0640)
print os.system("ls")
print os.path.isdir("temp")
os.rmdir("temp")

# 创建多层目录
os.system("ls -l")
print os.getcwd()
os.makedirs("./temp/a/b/c", 0777)

# 删除单层目录
if not os.path.exists("./temp/a/b/c"):
    os.makedirs("./temp/a/b/c")
    os.system("ls")
os.rmdir("./temp/a/b/c")
os.system("ls")
# 删除多级目录,从左到右都会被删除，需要传递一个完整的删除目录
if os.path.exists("./temp/a/b/"):
    os.removedirs("./temp/a/b/")
os.system("ls")

# 返回指定目录下所有文件

print os.listdir("/root/script/tmp")

# 修改权限以0开头
os.chmod("/root/script/tmp/file", 0777)

# 关于os.path的相关方法
# 判断是否为目录
print os.path.isdir("/root/script/tmp/file")

# 判断是否为文件
print os.path.isfile("/root/script/tmp/file")

# 判断目录文件是否存在
print os.path.exists("/root/script/tmp/file")

# 文件路径的获取方法
# 返回目录所在的路径
print os.path.dirname("/root/script/tmp/file")

# 目录切分，返回一个元组
print "the dir is ", os.path.split("/root/script/tmp/file")[0], "\nthe filename is  ", \
    os.path.split("/root/script/tmp/file")[1]

# 返回最后一级目录
print os.path.basename("/root/script/tmp/file")

# 拼接目录和文件
print os.path.join("/root/script/tmp/", "file")

# 文件的绝对路径
print os.path.abspath("./temp/a/file")

# 文件操作信息
# 获取文件或目录信息,返回很长的信息，选择需要的进行输出
# st_mode           : 权限模式
# st_ino            : inode number
# st_dev            : device
# st_nlink          : number of hard links
# st_uid            : 所有用户的user id
# st_gid            : 所有用户的group id
# st_size           : 文件的大小，以位为单位
# st_atime          : 文件最后访问时间
# st_mtime          : 文件最后修改时间
# st_ctime          : 文件创建时间
print os.stat("/root/script/tmp/temp/a/file")[6]

# 获取文件大小
print os.path.getsize("/root/script/tmp/temp/a/file")

# 获取文件最后访问时间
print os.path.getatime("/root/script/tmp/temp/a/file")

# 文件内容修改；对两个方法获取时间都有影响
# 文件权限，用户修改；只对getctime获取时间有影响
#
# 获取文件最后改变时间:
print os.path.getctime("/root/script/tmp/temp/a/file")

# 获取文件的最后修改时间
print os.path.getmtime("/root/script/tmp/temp/a/file")

# 其他方法
# 执行操作系统命令
os.system("touch a")

# 退出当前进程，需要添加退出状态
os._exit(11)
