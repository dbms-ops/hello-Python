# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
#
# UDP 编程服务端
#
#
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8090))

while True:
    data, addr = server.recvfrom(1024)
    print "client {} said: {}".format(addr, data.decode('utf-8'))
