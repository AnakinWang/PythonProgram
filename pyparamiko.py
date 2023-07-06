import paramiko

def testParamiko():
    # 创建 SSHClient 对象
    client = paramiko.SSHClient()

    local_path = r'E:\test.png'
    remote_path = '/home/tc/TrainData/TRobot_MLP/STDC/branches/test.png'
    _hostname = '172.17.1.232'
    _port = '22'
    _username = 'tc'
    _password = 'tc123456'

    try:
        # 自动添加主机到已知主机列表
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接到远程主机
        client.connect(hostname=_hostname, port=_port, username=_username, password=_password)

        # 执行命令
        stdin, stdout, stderr = client.exec_command('ls')

        # 读取命令输出
        output = stdout.read().decode()
        print('Output is {}'.format(output))

        sftp = client.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()



    finally:
        # 关闭 SSH 连接
        client.close()

if __name__=='__main__':
    testParamiko()
