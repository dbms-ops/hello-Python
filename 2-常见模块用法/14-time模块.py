# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
#
# time 模块：功能上面和datetime模块类似
# # !/data1/Python2.7/bin/python2.7
# #
# # UTC: 表示世界协调时间，格林尼治天文时间，世界标准时间，UTC + 8
# # DST：是一种为了节约能源而人为规定的时间制度，在夏季调快一个小时
# # 时间的表现形式：
# #   1、时间戳：以整型或者浮点数表示时间的一个秒为单位的时间间隔时间间隔的基础值、从1970年1月1号零点开始；
# #   2、元组：一种Python的数据结构，元组中包含9个整型内容
# #       year：
# #       month：
# #       day：
# #       hours：
# #       minutes：
# #       seconds：
# #       weekday：
# #       Julia da：
# #       flag：（1、-1、0）；
# #   3、字符串：
# #       %a	星期的英文单词的缩写：如星期一， 则返回 Mon
# #       %A	星期的英文单词的全拼：如星期一，返回 Monday
# #       %b	月份的英文单词的缩写：如一月， 则返回 Jan
# #       %B	月份的引文单词的缩写：如一月， 则返回 January
# #       %c	返回datetime的字符串表示，如03/08/15 23:01:26
# #       %d	返回的是当前时间是当前月的第几天
# #       %f	微秒的表示： 范围: [0,999999]
# #       %H	以24小时制表示当前小时
# #       %I	以12小时制表示当前小时
# #       %j	返回 当天是当年的第几天 范围[001,366]
# #       %m	返回月份 范围[0,12]
# #       %M	返回分钟数 范围 [0,59]
# #       %P	返回是上午还是下午–AM or PM
# #       %S	返回秒数 范围 [0,61]。。。手册说明的
# #       %U	返回当周是当年的第几周 以周日为第一天
# #       %W	返回当周是当年的第几周 以周一为第一天
# #       %w	当天在当周的天数，范围为[0, 6]，6表示星期天
# #       %x	日期的字符串表示 ：03/08/15
# #       %X	时间的字符串表示 ：23:22:08
# #       %y	两个数字表示的年份 15
# #       %Y	四个数字表示的年份 2015
# #       %z	与utc时间的间隔 （如果是本地时间，返回空字符串）
# #       %Z	时区名称（如果是本地时间，返回空字符串）
#
#
# # datetime 模块：和时间相关的模块

import time

# 返回当前时间的时间错，浮点数形势，不需要参数
c = time.time()
print c

# 将上面的浮点数转换成为元组
# 输出：
#   time.struct_time(tm_year=2019, tm_mon=12, tm_mday=29, tm_hour=4, tm_min=13, tm_sec=27, tm_wday=6, tm_yday=363,
#   tm_isdst=0)
# 得到的是一个格林尼治时间
utctime = time.gmtime(c)
print utctime

# 上面的时间转换成为当地时间
# 输出：
#   time.struct_time(tm_year=2019, tm_mon=12, tm_mday=29, tm_hour=12, tm_min=16, tm_sec=19, tm_wday=6, tm_yday=363,
#   tm_isdst=0)
localtime = time.localtime(c)
print localtime

# 将时间元组转换成为时间戳
localtimetuple = time.mktime(localtime)
print localtimetuple

# 将时间元组转换成为字符串
strtime = time.asctime(localtime)
print strtime

# 将时间戳转换成为字符串
strtime = time.ctime(c)
print strtime

# 自定义格式字符串
#
strtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print strtime

strtime = time.strftime("%Y-%m-%d %X", localtime)
print strtime

# 时间字符串转换成为元组
tupletime = time.strptime(strtime, "%Y-%m-%d %X")
print tupletime

# 程序等待一个时间
# 接收整型或者浮点型
time.sleep(0.3)

# 返回当前程序的CPU执行时间
# unix: 始终返回全部的运行时间
# Windows：从第二次开始、都是以第一个调用此函数的开始时间戳作为基数
# windows 时间计算如下：
start = time.clock()
print start
time.sleep(1)
end = time.clock()
print end

# unix时间计算：
print time.clock()
