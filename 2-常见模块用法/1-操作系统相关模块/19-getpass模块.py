# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
#
# getpass：简单的用于获取用户名和用户密码的模块
#

import getpass

# 获取当前用户的名称
print getpass.getuser()

# 从命令行获取用户输入的密码
if getpass.getpass() == "12345":
    print "log in successful"
else:
    print "invaild user"




if __name__ == '__main__':
    pass
    