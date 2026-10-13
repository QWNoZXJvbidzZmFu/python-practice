import paramiko
def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())
if __name__ == '__main__':
    import getpass
    #user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 22
    cmd = input('Enter command or <CR>: ') or ('id')
    ssh_command(ip, port, user, password,cmd)
#这个脚本(SSH)是一个自动化远程控制工具
#运行之后输入服务器的基本信息(用户ID，IP，密码...)就可以远程控制服务器

#SSH隧道是一种利用SSH加密连接来在本地和远程服务器之间安全传输数据的技术，
#建立了一个从本地机器到远程SSH服务器的加密通道，
#所有通过这个通道转发的数据都会被SSH加密，确保数据在网络传输过程中不被窃听或篡改。