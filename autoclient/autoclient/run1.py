import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname='10.21.10.103', port=22, username='poooy', password='163.comQ')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')

# 获取命令结果
result = stdout.read()

# 关闭连接
ssh.close()

value = result[0:10]
print(value)
