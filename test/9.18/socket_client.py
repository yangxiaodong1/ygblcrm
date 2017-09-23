# Author : July  Yang 
import socket

client = socket.socket()
client.connect(('localhost',9090))

while True:
    cmd = input(">>").strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    cmd_rec_size = client.recv(1024)
    recive_size =0
    recive_data = b''
    while recive_size <int(cmd_rec_size.encode()):
        data = client.recv(1024)
        recive_size+=len(data)
        recive_data+=data
    else:
        print()
client.close()







