# coding=utf-8
#
# 
# !/data1/Python2.7/bin/python27
# 
# 网络编程-服务端
#
#
import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
server.bind(('127.0.0.1', 8080))

# 监听
server.listen(5)

# 等待连接
while True:
    clientSocket, clientAddress = server.accept()
    receiveData = clientSocket.recv(1024)
    print 'receive data from {}: {}'.format(str(clientAddress), receiveData.decode('utf-8'))
