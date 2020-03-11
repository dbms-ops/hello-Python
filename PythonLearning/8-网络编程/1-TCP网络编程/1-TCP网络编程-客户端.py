# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 网络编程的基础知识
# 该文件对应的是客户端，创建TCP连接时，主动发起连接的是客户端；
# ；
#
import socket

# 创建一个socket
# socket.AF_INET: 指定IP连接的协议;
# socket.SOCK_STREAM: 指定使用面向流的连接协议;
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# 参数是一个元组：第一个参数为需要连接的IP地址，第二个参数为端口号
client.connect(('127.0.0.1', 8080))

client.send(b'what you send '.encode('utf-8'))

client.close()
