import socket
import threading   #让服务器能同时处理多个客户端连接
IP = '0.0.0.0'#监听本机所有网卡(网卡是电脑连接网络的硬件接口，比如WI-FI网卡，有线网卡，
              #回环网卡(虚拟网卡，自己连自己，对应IP127.0.0.1)
PORT = 9998
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建套接字
    server.bind((IP, PORT))#将套接字绑定到指定的IP和端口，让服务器在这里等待连接
    server.listen(5)#最多同时挂起5个未处理的请求
    print(f'[*] listening on {IP}:{PORT}')

    while True:   #让服务器持续等待客户端连接
        client, address = server.accept()   #等待客户端连接
        print(f'[*] accepted connection from {address[0]}:{address[1]}')#显示成功接收客户端的连接
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received {request.decode("utf-8")}')
        sock.send(b'Nice to meet you!')
if __name__ == '__main__':
    main()