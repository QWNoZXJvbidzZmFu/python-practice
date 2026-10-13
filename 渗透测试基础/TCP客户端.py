import socket
target_host = "0.0.0.0"
target_port = 9998    #HTTP协议默认端口号，用于网页访问
# create a socket object
client = socket.socket(socket.AF_INET,         socket.SOCK_STREAM)
#             ipv4网络套接字(AF_UNIX是Unix域套接字） 套接字类型：流式套接字，对应tcp协议

# connect the client
client.connect((target_host,target_port))  #连接客户端到服务器

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")
client.send(b"Hello,I'm a new client!")
#receive some data
response = client.recv(4096)
print(response.decode())
client.close()