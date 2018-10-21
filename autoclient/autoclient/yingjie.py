import subprocess
import importlib

importlib.import_module('a.b.c')

mode = "salt"  # ssh agent

# 中控机， 指定主机名或IP
if mode == 'salt':
    v1 = subprocess.getoutput('salt "c1.com" cmd.run "%s"' % 'ifconfig')
    v2 = subprocess.getoutput('salt "c1.com" cmd.run "%s"' % 'ls')
    v3 = subprocess.getoutput('salt "c1.com" cmd.run "%s"' % 'df')

# 中控机， 指定主机名或IP
elif mode == 'ssh':
    import paramiko
    private_key = paramiko.RSAKey.from_private_key("xxx")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="c1.com", port=22, username='sw', pkey=private_key)
    stdin, stdout, stderr = ssh.exec_command('ls')
    resultl = stdout.read()
    ssh.close()

