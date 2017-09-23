# Author : July  Yang 
import socket,os

server = socket.socket()
server.bind(('localhost',8080))
server.listen(20)

while True:
    conn,adress = server.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res)==0:
            cmd_res = 'cmd no output'

        conn.send(str(len(cmd_res).encode())).encode('utf-8')
        conn.send(cmd_res.encode('utf-8'))

server.close







