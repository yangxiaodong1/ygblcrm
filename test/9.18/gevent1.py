# Author : July  Yang 

# import  socket ,gevent
# from gevent import socket,monkey
# monkey.patch_all()
#
# # 服务器连接
# def server(port):
#     s = socket.socket()
#     s.bind(('0.0.0.0',port))
#     s.listen(20)
#     while True:
#         cli,address = s.accept()
#         gevent.spawn(handle_request,cli)
#
# def handle_request(conn):
#     try :
#         while True:
#             data = conn.recv(1024)
#             conn.send(data)
#
#     except Exception as e:
#
#     finally:
#         conn.close()




