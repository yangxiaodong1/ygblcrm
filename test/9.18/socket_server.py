# Author : July  Yang 
import socket,os

server =socket.socket()
server.bind(('localhost',9090))
server.listen(20)
# 多册接受数据

while True:
    conn,adress = server.accept()
    while True:
        # 等待新的指令
        data = conn.recv(1024)
        if not data:
            print('客户端断开了')
            break
        #执行命令data
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res)==0:
            cmd_res = 'cmd 没有'
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))
        conn.send(cmd_res.encode('utf-8'))

server.close()






