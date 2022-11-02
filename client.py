import socket
# 新建socket
client = socket.socket()
# 连接服务端（注意，IP和端口要和服务端一致）
client.connect(('127.0.0.1', 8999))

while True:
    content = input('>>> ')
    # 发送内容，注意发送的是字符串
    client.send(bytes(content, encoding='utf-8'))
    content = client.recv(1024)
    print(str(content, encoding='utf-8'))

client.close()