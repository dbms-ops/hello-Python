# coding=utf-8
#
#
# !/data1/Python2.7/bin/python27
# 
# UDP网络编程：建立的网络连接是不可靠的，建立面向无连接的协议，不需要建立连接，只需要对方的IP和端口号；
# UDP：传输数据不可靠，但是传输数据快速；
#

import socket

# 建立连接：
#
# ;
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = str(input('please input data: '))
    client.sendto(data.encode('utf-8'), ('127.0.0.1', 8090))
