# 客户端
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 8080))
print("客户端启动")
while True:
  client_data = input('>>>').strip()
  if not client_data:
    continue
  phone.send(client_data.encode('utf-8'))
  if client_data == 'q':break

  from_server_data = phone.recv(1024)
  print(from_server_data.decode('utf-8'))

phone.close()