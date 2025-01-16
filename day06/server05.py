# 基于UDP协议的通信
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket.SOCK_DGRAM 表示使用UDP协议
udp_socket.bind(('127.0.0.1', 8080))
# 接收消息
msg, addr = udp_socket.recvfrom(1024)
print(addr,':',msg.decode('utf-8'))

# 回复消息
udp_socket.sendto(msg.upper(),addr)

# 关闭Socket
udp_socket.close()