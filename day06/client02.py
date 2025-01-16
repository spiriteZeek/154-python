# 01的通信是单次的，通信完成一次以后，就关闭连接。我们可以加上while循环，让他们循环通信
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))

while True:     # 客户端这边也循环发送信息，并且等待接收
    client_data = input('>>> ')
    if client_data == 'q':
        break
    phone.send(client_data.encode('utf-8'))
    
    from_server_data = phone.recv(1024)
    print(from_server_data.decode('utf-8'))

phone.close()

