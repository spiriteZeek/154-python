# 远程代码执行
import socket
import subprocess   # 通过sunprocess模块来执行cmd命令

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8080))
phone.listen(5)

while True:  # 循环连接客户端
    conn, client_addr = phone.accept()
    print(client_addr)

    while True:
        try:
            cmd = conn.recv(1024)
            ret = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            correct_msg = ret.stdout.read()
            error_msg = ret.stderr.read()
            print(correct_msg, error_msg)
            conn.send(correct_msg + error_msg)
        except ConnectionResetError:
            break
conn.close()
phone.close()