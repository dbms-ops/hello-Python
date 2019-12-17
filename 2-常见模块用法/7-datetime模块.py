# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
# author: Lixun
# datetime 模块：和时间相关的模块

from datetime import date

# 当前日期
print "today(): ", date.today()

# 返回时间戳的日期对象
print 'fromtimestamp(1491448600): ', date.fromtimestamp(1491448600)

# 返回对应公历序数的日期对象
print 'date.fromordinal(1)', date.fromordinal(1234561)


# 对象、属性、方法
time = date(2017,04,06)

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





if __name__ == '__main__':
    pass
    