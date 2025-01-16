import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))

phone.send('hello'.encode('utf-8')) # 连接以后，直接给服务端发消息

from_server_data = phone.recv(1024) # 通过recv方法等待服务端的回信

print(from_server_data) # 打印服务端的回信
phone.close() # 关闭连接