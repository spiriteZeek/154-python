# 基于UDP协议的通信
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('127.0.0.1', 8080)

# 发送消息
msg = input(">>>")
udp_socket.sendto(msg.encode("utf-8"), ip_port)

# 接收消息
back_msg, addr = udp_socket.recvfrom(1024)
print(back_msg.decode("utf-8"))

udp_socket.close()