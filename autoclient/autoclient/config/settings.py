"""
用户算定义配置文件
"""
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER = 'root'
PWD = "sdsdf"

MODE = "AGENT"  # salt, ssh

DEBUG = True
SSH_USER = "root"
SSH_PWD = "root"
SSH_KEY = "/xxx/xxx/xx"
SSH_PORT = 22

PLUGINS_DICT = {
    'basic': "src.plugins.basic.Basic",
    'board': "src.plugins.board.Board",
    'cpu': "src.plugins.cpu.Cpu",
    'disk': "src.plugins.disk.Disk",
    'memory': "src.plugins.memory.Memory",
    'nic': "src.plugins.nic.Nic",
}

API = "http://www.oldboyedu.com"

CERT_PATH = os.path.join(BASEDIR, 'config', 'cert')