# Author : July  Yang 
import socket

client =socket.socket()
client.connect(('localhost',8080))

while True:
    cmd = input('>>>').strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    cmd_recv_size = client.recv(1024)
    recive_size = 0
    recive_data = b''
    while recive_size <cmd_recv_size:
        data = client.recv(1024)
        recive_size +=len(data)
        recive_data +=data
    else:
        print()
client.close()







