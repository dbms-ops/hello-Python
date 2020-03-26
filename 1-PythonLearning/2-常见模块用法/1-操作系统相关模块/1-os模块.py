#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/19 16:48
# @user: Administrator
# @fileName: os模块.py
# @description: os 模块 用于执行操作系统相关的命令
#

import os


def osName():
    # 操作系统类型
    print os.name


def osUname():
    # 打印操作系统的详细信息，windows不支持
    print os.uname()
    print os.uname()[0]
    print os.uname()[1]
    print os.uname()[2]
    print os.uname()[3]
    print os.uname()[4]

    print type(os.uname())


def osEnv():
    # 打印操作系统的环境变量
    print os.environ


def osEnviron():
    # 获取某个详细的环境变量
    print os.environ.get("SSH_CLIENT")


def osGetcwd():
    # print "获取当前脚本工作的目录路径: "
    print os.getcwd()


def osChdir():
    # "修改当前目录为path"
    os.chdir("/root/script/tmp/")
    print os.getcwd()


def osSystem():
    # 执行操作系统命令
    os.system("ls")
    print os.getcwd()


def osPathExists():
    # 创建目录:用于创建单层级别目录
    # 不传递 mode 关键字
    if not os.path.exists("temp"):
        os.mkdir("temp", 0640)
    print os.system("ls")
    print os.path.isdir("temp")
    os.rmdir("temp")


def osMkdirs():
    # 创建多层目录
    os.system("ls -l")
    print os.getcwd()
    os.makedirs("./temp/a/b/c", 0777)


def osRmdirs():
    # 删除单层目录
    if not os.path.exists("./temp/a/b/c"):
        os.makedirs("./temp/a/b/c")
        os.system("ls")
    os.rmdir("./temp/a/b/c")
    os.system("ls")


def osRemoveDirs():
    # 删除多级目录,从左到右都会被删除，需要传递一个完整的删除目录
    if os.path.exists("./temp/a/b/"):
        os.removedirs("./temp/a/b/")
    os.system("ls")


def osRename():
    # 文件或者目录的重命名操作
    os.rename('./temp/a/b', './temp/a/c')


def osRemove():
    # 删除普通文件
    os.remove("./temp/a/b")


def osLexists():
    # 用于处理连接文件，判断 path 所链接的文件是否存在
    os.path.lexists('./temp/a/b.txt')


def osListDirs():
    # 返回指定目录下所有文件
    print os.listdir("/root/script/tmp")


def osChmod():
    # 修改权限以0开头
    os.chmod("/root/script/tmp/file", 0777)


def osPathIsdirs():
    # 关于os.path的相关方法
    # 判断是否为目录
    print os.path.isdir("/root/script/tmp/file")


def osIsFile():
    # 判断是否为文件
    print os.path.isfile("/root/script/tmp/file")


def osExists():
    # 判断目录文件是否存在
    print os.path.exists("/root/script/tmp/file")


def osDirname():
    # 文件路径的获取方法
    # 返回目录所在的路径
    print os.path.dirname("/root/script/tmp/file")


def osSplit():
    # 目录切分，返回一个元组
    print "the dir is ", os.path.split("/root/script/tmp/file")[0], "\nthe filename is  ", \
        os.path.split("/root/script/tmp/file")[1]


def osSplitext():
    # 获取文件的扩展名,没有扩展名为空
    path = "/root/script/tmp/file.txt"
    print os.path.splitext(path)


def osBasename():
    # 返回最后一级目录
    print os.path.basename("/root/script/tmp/file")


def osJoin():
    # 拼接目录和文件
    print os.path.join("/root/script/tmp/", "file")


def osAbspath():
    # 文件的绝对路径
    print os.path.abspath("./temp/a/file")


def osStats():
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


def osGetsize():
    # 获取文件大小[字节]
    print os.path.getsize("/root/script/tmp/temp/a/file")


def osGetatime():
    # 获取文件最后访问时间
    print os.path.getatime("/root/script/tmp/temp/a/file")


def osGetctime():
    # 文件内容修改；对两个方法获取时间都有影响
    # 文件权限，用户修改；只对getctime获取时间有影响
    #
    # 获取文件最后改变时间:
    print os.path.getctime("/root/script/tmp/temp/a/file")

    # 获取文件的最后修改时间
    print os.path.getmtime("/root/script/tmp/temp/a/file")


def osSystemCommand():
    # 其他方法
    # 执行操作系统命令
    os.system("touch a")


def osExit():
    # 退出当前进程，需要添加退出状态
    os._exit(11)


def osPrintInfo():
    print os.ctermid()
    print os.getegid()
    print os.getgroups()
    print os.getlogin()
    print os.getpid()
    print os.getresuid()
    # os.setegid(1001)
    # os.setgid(1000)
    print os.getpid()


def main():
    osPrintInfo()


if __name__ == '__main__':
    main()
