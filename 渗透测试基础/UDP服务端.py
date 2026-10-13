import socket

server_host = "127.0.0.1"
server_port = 9997

# 创建UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口
server.bind((server_host, server_port))
print(f"UDP服务端已启动，监听 {server_host}:{server_port}")

while True:
    # 接收客户端数据
    data, addr = server.recvfrom(1024)
    print(f"收到来自 {addr} 的数据: {data.decode()}")
    # 回复客户端
    server.sendto(b"Server received: " + data, addr)