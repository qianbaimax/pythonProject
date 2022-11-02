import socket
# 新建socket
server = socket.socket()
# 绑定IP和端口
server.bind(('127.0.0.1', 8999))
# 监听连接
server.listen(5)
# 接受连接
s, addr = server.accept()
print('connect addr: {}'.format(addr))

while True:
    content = s.recv(1024)
    if len(content) == 0:
        break
    s.send(content)
    # 接受来自客户端的消息，并编码打印出来
    print(str(content, encoding='utf-8'))
s.close()


