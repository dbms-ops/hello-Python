#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# date: 2020-1-16 16:57
# user: Administrator
# description: 脚本用于处理文件，包括文件的读写操作；
#

#
# 文件的操作是通过文件描述符来进行的
#   文件的操作包括读文件、写文件
#   读文件：
#     打开文件：open(filePath,flag): 文件的打开方式，以及文件的打开标志
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


def read_all(file_path):
    """
    Read the entire contents of the file
    :param file_path: File file_path, must exist
    :return: No return value
    """
    # 打开文件
    # file_handler = open(file_path,'r',encoding='utf-8',errors='ignore')
    file_handler = open(file_path, 'r')

    # 读取文件内容
    # 1、读取文件的全部内容
    file_handler.read()
    file_handler.close()


def read_character(file_path):
    # 打开文件
    """
    Read the specified number of characters
    :param file_path: File file_path, must exist
    :return: No return value
    """
    # file_handler = open(file_path,'r',encoding='utf-8',errors='ignore')
    file_handler = open(file_path, 'r')
    # 2、读取指定的字符数
    file_handler.read(10)
    file_handler.close()


def read_line(file_path):
    # 打开文件
    """
    Read the specified number of characters in a line
    :param file_path: File file_path, must exist
    :return: No return value
    """
    # file_handler = open(file_path,'r',encoding='utf-8',errors='ignore')
    file_handler = open(file_path, 'r')
    # 3、读取整行，包括'\n'字符。

    # 读取一行中的指定字符数
    str_line = file_handler.readline(10)
    file_handler.close()


def read_all_line(file_path):
    """
    Read all lines in file_path file
    :param file_path: File file_path, must exist
    :return: No return value
    """
    # file_handler = open(file_path,'r',encoding='utf-8',errors='ignore')
    file_handler = open(file_path, 'r')
    # 4、读取所有行，并且返回列表,n 表读取的行数，向上取整
    # 通常读取行数比较常见，很少有进行字符数的读取
    file_list = file_handler.readlines(10)

    # 修改文件描述符的位置
    file_handler.seek(10)

    # 关闭文件描述符
    file_handler.close()


# 完整的文件读取过程
def read_file_complete(file_path):
    """
    The complete process of file reading
    :param file_path: File file_path, must exist
    :return: No return value
    """
    try:
        file_handler = open(file_path, 'r')
        print file_handler.read()
    finally:
        if file_handler:
            file_handler.close()


def file_read_simple(file_path):
    """
    The easiest way to read files
    :param file_path: File file_path, must exist
    :return: No return value
    """
    with open(file_path, 'r') as file_handler:
        print file_handler.read()


def single_line_read_while(file_path):
    """
    Reading the contents of a file using a while loop
    :param file_path: File file_path, must exist
    :return: No return value
    """
    lineNum = 0
    with open(file_path, 'r') as file_handler:
        while True:
            line = file_handler.readline()
            if not line:
                break
            # 用于去掉文件末尾的换行符
            print line.strip('\n')
            lineNum += 1
    print lineNum


def single_line_read_for(file_path):
    """
    Reading the contents of a file using a for loop
    :param file_path: File file_path, must exist
    :return: No return value
    """
    lineNum = 0
    with open(file_path, 'r') as file_handler:
        for line in file_handler:
            # 用于去掉末尾的换行
            print line[0:-1]
            lineNum += 1
    print lineNum


def list_line_read(file_path):
    with open(file_path, 'r') as lineRead:
        lineList = [line.strip('\n') for line in lineRead.readlines()]
        print lineList


def big_file_read_chunck(fileObj, chunck_size):
    """
    Coroutines to read files according to block size
    :param fileObj: File descriptor
    :param chunck_size: Block size per read
    :return: Returns the data read each time
    """
    while True:
        data = fileObj.read(chunck_size)
        if not data:
            break
        yield data


def big_file_read_line(fileObj):
    """
    Coroutines to read files according to block size
    :param fileObj: File descriptor
    :param chunck_size: Block size per read
    :return: Returns the data read each time
    """
    while True:
        data = fileObj.readline()
        if not data:
            break
        yield data


def main():
    file_path = "/etc/snmp/yyms_agent_db_scripts/db_6301.conf"
    single_line_read_while(file_path)


if __name__ == '__main__':
    main()
