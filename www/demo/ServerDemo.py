
'TCP服务器'

import socket
import threading

mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建基于ipv4和TCP的socket
mySocket.bind(('127.0.0.1',9888))#监听端口
mySocket.listen(5)#监听端口 传入的参数指定等待连接的最大数量
print('Waiting for connection...')


def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('张伟大傻逼')
    while True:
        data=sock.recv(1024)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send('大傻逼张伟')
    sock.close()

while True:
    sock,addr=mySocket.accept()#accept()会等待并返回一个客户端的连接
    thr=threading.Thread(target=tcplink,args=(socket,addr))
    thr.start()

