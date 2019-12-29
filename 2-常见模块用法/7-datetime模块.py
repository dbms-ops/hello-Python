# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7
#
# UTC: 表示世界协调时间，格林尼治天文时间，世界标准时间，UTC + 8
# DST：是一种为了节约能源而人为规定的时间制度，在夏季调快一个小时
# 时间的表现形式：
#   1、时间戳：以整型或者浮点数表示时间的一个秒为单位的时间间隔时间间隔的基础值、从1970年1月1号零点开始；
#   2、元组：一种Python的数据结构，元组中包含9个整型内容
#       year：
#       month：
#       day：
#       hours：
#       minutes：
#       seconds：
#       weekday：
#       Julia da：
#       flag：（1、-1、0）；
#   3、字符串：
#       %a	星期的英文单词的缩写：如星期一， 则返回 Mon
#       %A	星期的英文单词的全拼：如星期一，返回 Monday
#       %b	月份的英文单词的缩写：如一月， 则返回 Jan
#       %B	月份的引文单词的缩写：如一月， 则返回 January
#       %c	返回datetime的字符串表示，如03/08/15 23:01:26
#       %d	返回的是当前时间是当前月的第几天
#       %f	微秒的表示： 范围: [0,999999]
#       %H	以24小时制表示当前小时
#       %I	以12小时制表示当前小时
#       %j	返回 当天是当年的第几天 范围[001,366]
#       %m	返回月份 范围[0,12]
#       %M	返回分钟数 范围 [0,59]
#       %P	返回是上午还是下午–AM or PM
#       %S	返回秒数 范围 [0,61]。。。手册说明的
#       %U	返回当周是当年的第几周 以周日为第一天
#       %W	返回当周是当年的第几周 以周一为第一天
#       %w	当天在当周的天数，范围为[0, 6]，6表示星期天
#       %x	日期的字符串表示 ：03/08/15
#       %X	时间的字符串表示 ：23:22:08
#       %y	两个数字表示的年份 15
#       %Y	四个数字表示的年份 2015
#       %z	与utc时间的间隔 （如果是本地时间，返回空字符串）
#       %Z	时区名称（如果是本地时间，返回空字符串）
#  datetime 是 time 模块的升级版本，接口更加直观，更加容易调用
#  常见的类：
#   datetime：时间和日期
#   timedelta：主要用于计算时间的跨度
#   tzinfo：时区
#   time：关注时间
#   date：关注日期
#   ；


# datetime 模块：和时间相关的模块

from datetime import date

# 当前日期
print "today(): ", date.today()

# 返回时间戳的日期对象
print 'fromtimestamp(1491448600): ', date.fromtimestamp(1491448600)

# 返回对应公历序数的日期对象
print 'date.fromordinal(1)', date.fromordinal(1234561)

# 对象、属性、方法
time = date(2017, 04, 06)

# 返回date对象的年份
print 'time.year', time.year

# 返回date对象的月份
print 'time.month', time.month

# 返回date对象的日
print 'time.day', time.day

# 返回date对象的struct_time结构
print 'time.toordinal', time.toordinal()

# 返回一星期中的第几天,星期一是0
print 'time.isoweekday', time.isoweekday()

# 返回一个元组(年份, 这一年的第几周, 周几)
print 'time.isocalendar', time.isocalendar()

# 以ISO 8601格式‘YYYY-MM-DD’返回date的字符串形式
print 'time.isoformat', time.isoformat()

# 返回一个表示日期的字符串
print 'time.ctime', time.ctime()

# 返回指定格式的日期字符串
print 'time.strftime("%Y-%m-%d")', time.strftime('%Y-%m-%d')

# 替换
print 'time.replace(year=2012, month=12) :', time.replace(year=2012, month=12)

# datetime.time: 表示一个(当地)时间对象，与任何特定的日期无关，并且可以通过tzinfo(时区)对象进行调整
#

from datetime import time

t = time(12, 10, 30, 50)

# time对象小时数
print 't.hour:', t.hour

# time对象分钟数
print 't.minute:', t.minute

# time对象秒数
print 't.second:', t.second

# time对象微秒数
print 't.microsecond:', t.microsecond

# 返回ISO 8601格式的时间字符串
print 't.isoformat():', t.isoformat()

# 返回指定格式的时间格式
print 't.strftime("%H:%M:%S:%f"):', t.strftime("%H:%M:%S:%f")

# 替换
print 't.replace(hour=23, minute=0):', t.replace(hour=23, minute=0)

# datetime 的 datetime方法
# datetime对象包含date对象和time对象的所有信息
from datetime import datetime, time, date

# 返回本地当前的时间datetime对象
print 'datetime.today():', datetime.today()

# 返回本地当前的日期和时间的datetime对象
print 'datetime.now():', datetime.now()

# 返回当前UTC日期和时间的datetime对象
print 'datetime.utcnow():', datetime.utcnow()

# 返回对应时间戳的datetime对象
print 'datetime.fromtimestamp(1491468000):', datetime.fromtimestamp(1491468000)

# 同date.fromordinal类似
print 'datetime.fromordinal(699000):', datetime.fromordinal(699000)

# 拼接date和time
print 'datetime.combine(date(2012,12,12), time(12,12,12)):', datetime.combine(date(2012, 12, 12), time(23, 59, 59))

# 将特定格式的日期时间字符串解析成datetime对象
print 'datetime.strptime("2012-12-10", "%Y-%m-%d"):', datetime.strptime("2012-12-10", "%Y-%m-%d")

from datetime import datetime

d = datetime(2017, 04, 06, 12, 10, 30)

# 从datetime中拆分出date
print 'd.date():', d.date()

# 从datetime中拆分出time
print 'd.time():', d.time()

# 从datetime中拆分出具体时区属性的time
print 'd.timetz()', d.timetz()

# 替换
print 'd.replace(year=2016):', d.replace(year=2016)

# 时间数组,即struct_time结构
print 'd.timetuple():', d.timetuple()

# 和date.toordinal一样
print 'd.toordinal():', d.toordinal()

# 和date.weekday一样
print 'd.weekday():', d.weekday()

# 和date.isoweekday一样
print 'd.isoweekday():', d.isoweekday()

# 和date.isocalendar一样
print 'd.isocalendar():', d.isocalendar()

# 同上
print 'd.isoformat():', d.isoformat()

# 同上
print 'd.ctime():', d.ctime()

# 同上
print 'd.strftime("%Y-/%m-%d %H:%M:%S"):', d.strftime('%Y-%m-%d %H:%M:%S')

# 常见应用
# 时间戳转日期
timestamp = 1491550000
print datetime.fromtimestamp(timestamp)
print datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

# 字符串转日期
str = '2012-12-10'
print datetime.strptime(str, '%Y-%m-%d')
print datetime.strptime(str, '%Y-%m-%d').strftime('%Y/%m/%d')

# 计算时间间隔日期
from datetime import datetime, timedelta

td = datetime.today()
print td
print td - timedelta(days=2)
print td + timedelta(days=2)

import datetime

start = datetime.datetime(2008, 10, 1, 10, 28, 25, 123456)
end = datetime.datetime.now()
interval = end - start
print interval.days, interval.seconds

if __name__ == '__main__':
    pass
