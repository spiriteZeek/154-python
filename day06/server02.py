import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)
print("服务端开启成功")

conn, client_addr = phone.accept()
print(conn, client_addr)

while True:
  try:
    from_client_data = conn.recv(1024)
    print(from_client_data.decode('utf-8'))

    conn.send(from_client_data.upper())
  except ConnectionResetError:
    break

conn.close()
phone.close()