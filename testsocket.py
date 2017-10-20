#coding:utf-8
import socket
import time
def getIP():
    #链接服务端ip和端口
    ip_port = ('121.42.227.3',3838)
    #生成一个句柄
    sk = socket.socket()
    #请求连接服务端
    sk.connect(ip_port)
    #发送数据
    sk.sendall(bytes('wiseweb\r\n'))
    proxyIP=sk.makefile().readline()
    #打印接受的数据
    print(proxyIP)
    #关闭连接
    sk.close()
    return proxyIP

def main():
    while True:

        ip = getIP()

        time.sleep(2)
if __name__ == '__main__':
    main()


'''
# -*- coding: utf-8 -*-
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))

# 发送数据:
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


# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
print(html.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
'''
