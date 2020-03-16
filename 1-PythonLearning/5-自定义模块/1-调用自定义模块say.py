# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
# date: 2020/1/16 16:57
# user: Administrator
# description: 用与调用自定义模块
#

# 用于调用自定义模块 say
#

# 引入自定模块
# 引入自定义模块不需要加入.py
# 多次引入只会被引入一次
import say

# 使用模块中的内容
say.saygood()

# from import 引入自定义模块
# 从指定的模块中引入一个指定的部分到当前命名空间
from say import saynice

saynice()

# from import *
# 不建议使用这种方式引入模块
# 用于将一个模块中的所有内容导入到当前命名空间
from say import *

saynice()
sayhello()
