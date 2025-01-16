# 单个客户端与服务端通信
import socket
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 初始化socket对象，可以理解为买电话
# socket_family可以是AF_UNIX或AF_INET。socket_type可以是SOCK_STREAM或SOCK_DGRAM。

phone.bind(('127.0.0.1', 8080)) #0~65535 1024之前是系统已经分配好的 绑定手机卡，绑定后才能接听别人的电话
print("服务端开启成功")
phone.listen(5) # 同一时刻最多有5个电话在排队

conn, client_addr = phone.accept() # 调用accept阻塞代码，等待客户端的连接，可以理解为接电话
print(conn, client_addr, sep="\n") # 如果有客户端连接，获取conn TCP连接对象， client_addr客户端地址
print("客户端连接成功")

from_client_data = conn.recv(1024) # 调用recv方法来接受客户端发来的数据，1024代表最大接收的字节数
print("from_client_data: ", from_client_data.decode('utf-8')) # 打印接收的信息

conn.send(from_client_data.upper()) # 调用send方法来给客户端回复信息

conn.close() # 断开TCP连接，可以理解为挂电话

phone.close() # 关闭socket对象，可以理解为关机