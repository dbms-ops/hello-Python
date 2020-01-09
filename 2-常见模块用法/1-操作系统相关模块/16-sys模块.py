# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
#
#
# sys 模块
#   提供对于解释器维护的变量进行访问
import sys

# 获取命令行参数的列表
print sys.argv[0]
print sys.argv

# 输出字节序的方式：大段排序或者是小段排序
print sys.byteorder

# 给出了编译到此Python解释器中的所有模块的名称
print sys.builtin_module_names

# 一个字符串，其中包含与Python解释器有关的版权
print sys.copyright

#
print sys.exc_info()

# 安装了Python解释器的目录
print sys.exec_prefix

# Python可执行文件的绝对路径
print sys.executable

# 退出 Python 解释器
# sys.exit(12)

# 获取当前文件系统对于文件的编码方式
print sys.getfilesystemencoding()

# 返回对象的引用计数；
print sys.getrefcount(str)

# 返回对象的大小，对于第三方对象大小不一定准确
print sys.getsizeof(str)

# Python支持的最大常规整数
print sys.maxint


# Py_ssize_t类型支持的最大正整数
print sys.maxsize

# 指定模块的搜索路径,该列表可以修改
print sys.path

# 查询平台标识符
#   linux2、win32、darwin、等
print sys.platform

# Python 解释器对应的路径信息
print sys.prefix

# 设置默认的编码格式
# sys.setdefaultencoding("utf-8")

# 标注输入信息
print sys.stdin, sys.stdout, sys.stderr

# version_info
print sys.version_info
