import socket   #实现网络通信
import argparse #解析命令行参数
import shlex    #安全分割命令字符串，避免命令注入风险
import subprocess#执行系统命令并获得输出
import sys
import textwrap
import threading#多线程连接
def execute(cmd):
    cmd = cmd.strip()#清理输入的多余空白
    if not cmd:
        return None
                                   #安全拆分命令        把错误信息合并到输出
    output = subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
    return output.decode()#把系统命令返回的结果(字节类型)转换为字符串

class NetCat:
    def __init__(self,args,buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    def run(self):
        if self.args.listen:#如果NetCat对象是接收方，run就执行listen函数
            self.listen()
        else:               #如果是发送方，就执行send函数
            self.send()
    def send(self):
        self.socket.connect((self.args.target,self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response,end='')
                buffer = input('')
                buffer += '\n'
                self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket,_ = self.socket.accept()
            client_thread = threading.Thread(target=self.handle,args=(client_socket,))
            client_thread.start()
    def handle(self,client_socket):
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server killed {e}')
                    self.socket.close()
                    sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c #commend shell
        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt # upload to file
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
        echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
        netcat.py -t 192.168.1.108 -p 5555 # connect to server
        '''))
    parser.add_argument('-c', '--command',action='store_true',help='command shell')
    parser.add_argument('-e', '--execute',help='execute specified command')
    parser.add_argument('-l','--listen',action='store_true',help='listen')
    parser.add_argument('-p','--port',type=int,default=5555,help='specified port')
    parser.add_argument('-u','--upload',help='upload file')
    parser.add_argument('-t', '--target',default='192.168.1.203',help='specified IP')
    args = parser.parse_args()#解析命令行输入的参数，将结果存入args
    if args.listen:            #判断是否为监听模式
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc = NetCat(args,buffer.encode())
    nc.run()