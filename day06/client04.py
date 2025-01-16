import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))
while True:
    msg = input('>>: ').strip()
    if not msg:continue
    if msg == 'q':break
    phone.send(msg.encode('utf-8'))

    # 收消息
    from_server_data = phone.recv(1024)
    print(from_server_data.decode('utf-8'))

phone.close()