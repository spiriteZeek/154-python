# 示例三：循环连接通信
# 比如淘宝的客服机器人，机器人会一直存在，等待下一个人连接。

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)
print("启动服务")

while True:   # 将accept方法也加入到循环体中，让他循环的监控客户端的连接
  conn, client_addr = phone.accept()
  print(conn, client_addr, sep="\n")

  while True:
    try:
      from_client_data = conn.recv(1024)
      if not from_client_data:
        break
      print(f"客户端{client_addr}发来的消息{from_client_data.decode()}")

      conn.send(from_client_data.upper())
    except Exception:
      break

conn.close()
phone.close()