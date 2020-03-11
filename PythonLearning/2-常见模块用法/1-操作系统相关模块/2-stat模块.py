# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7


# stat模块主要用于根据os.stat读出的属性信息进行判断

import os
import stat

# 常见的用法就是下面几种，下面的大部分功能os模块都是可以替换的
mode = os.stat("/root/script/tmp/temp/a/file")
if stat.S_ISREG(mode):
    print "Regular file"
elif stat.S_ISLNK(mode):
    print "Shortcut"
elif stat.S_ISSOCK(mode):
    print "Socket"
elif stat.S_ISFIFO(mode):
    print "Named pipe."
elif stat.S_ISBLK(mode):
    print "Block special device."
elif stat.S_ISCHR(mode):
    print 'Character special device.'
elif stat.S_ISDIR(mode):
    print "directory."
else:
    print "I don\'t know"
