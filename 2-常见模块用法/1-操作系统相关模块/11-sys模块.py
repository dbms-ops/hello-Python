#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-02-16 19:24
# user: linux
# description:
# sys 模块
#   提供对于解释器维护的变量进行访问
import sys


def get_argv():
    # 获取命令行参数的列表
    print sys.argv[0]
    print sys.argv


def get_byteorder():
    # 输出字节序的方式：大段排序或者是小段排序
    print sys.byteorder


def get_builtin_module_names():
    # 给出了编译到此Python解释器中的所有模块的名称
    print sys.builtin_module_names


def get_copyright():
    # 一个字符串，其中包含与Python解释器有关的版权
    print sys.copyright


def get_exc_info():
    #
    print sys.exc_info()


def get_exec_prefix():
    # 安装了Python解释器的目录
    print sys.exec_prefix


def get_executable():
    # Python可执行文件的绝对路径
    print sys.executable


def exit_help():
    # 退出 Python 解释器
    sys.exit(12)


def get_getfilesystemencoding():
    # 获取当前文件系统对于文件的编码方式
    print sys.getfilesystemencoding()


def get_getrefcount():
    # 返回对象的引用计数；
    print sys.getrefcount(str)


def get_getsizeof():
    # 返回对象的大小，对于第三方对象大小不一定准确
    print sys.getsizeof(str)


def get_maxint():
    # Python支持的最大常规整数
    print sys.maxint


def get_maxsize():
    # Py_ssize_t类型支持的最大正整数
    print sys.maxsize


def get_path():
    # 指定模块的搜索路径,该列表可以修改
    print sys.path


def get_platform():
    # 查询平台标识符
    #   linux2、win32、darwin、等
    print sys.platform


def get_prefix():
    # Python 解释器对应的路径信息
    print sys.prefix


def set_setdefaultencoding():
    # 设置默认的编码格式
    sys.setdefaultencoding("utf-8")


def std_help():
    # 标注输入信息
    print sys.stdin, sys.stdout, sys.stderr


def get_version():
    # version_info
    print sys.version_info


def main():
    get_argv()


if __name__ == '__main__':
    main()
