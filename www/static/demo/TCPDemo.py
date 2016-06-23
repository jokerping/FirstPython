
'访问无服务器'

import socket
#创建socket对象
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    # 简历连接
    s.connect(('www.sina.com.cn', 80))
    # 发送数据
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    header,html=data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open('/Users/1039soft/Desktop/sina.html','wb') as f:
        f.write(html)
