# -*-coding:utf-8-*-
# !/data1/Python2.7/bin/python2.7

#
# 文件的操作是通过文件描述符来进行的
#   文件的操作包括读文件、写文件
#   读文件：
#     打开文件：open(path,flag): 文件的打开方式，以及文件的打开标志
#        flag：
#         r：只读方式打开文件，文件描述符位于开头
#         rb：以二进制格式打开文件，用于只读操作
#         r+：打开一个文件用于进行读写操作，文件描述符位于开头
#         w：打开一个文件用于写入；文件存在执行覆盖，如果不存在则创建新文件
#         wb：打开一个文件用于写入二进制，如果文件存在，执行覆盖，如果不存在，创建新的文件
#         w+:打开一个文件用于进行读写操作，如果文件存在执行覆盖，否则创建
#         a: 用于在文件尾部执行追加操作；如果文件存在，从末尾开始追加；
#         a+:打开一个文件用于进行读写，文件描述符位于末尾’
#         encoding: 表示文件的编码，常因为utf-8
#         errors：比较常用，用于指定对于文件打开错误的处理方式
#     读取文件内容
#     关闭文件
#


# 打开文件
path = '/root/tmp/pycharm_project_179/test'

# file_handler = open(path,'r',encoding='utf-8',errors='ignore')
file_handler = open(path, 'r')

# 读取文件内容
# 1、读取文件的全部内容
file_handler.read()

# 2、读取指定的字符数
file_handler.read(10)

# 3、读取整行，包括'\n'字符。

# 读取一行中的指定字符数
str_line = file_handler.readline(10)

# 4、读取所有行，并且返回列表,n 表读取的行数，向上取整
# 通常读取行数比较常见，很少有进行字符数的读取
file_list = file_handler.readlines(10)

# 修改文件描述符的位置
file_handler.seek(10)

# 关闭文件描述符
file_handler.close()
# 完整的文件读取过程
try:
    file_handler = open(path, 'r', encoding='utf-8')
    print file_handler.read()
finally:
    if file_handler:
        file_handler.close()

# 更简单的文件读取方式
with open(path, 'r', encoding='utf-8') as file_handler:
    print file_handler.read()

if __name__ == '__main__':
    pass
