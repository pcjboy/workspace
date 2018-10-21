__author__ = 'administrator'
# ###########################Agent ###########################
import subprocess

v1 = subprocess.getoutput('ipconfig')
valuel = v1[20:30]

v2 = subprocess.getoutput('dir')
value2 = v2[0:5]


# 连接数据库，写到数据库

url = "http://127.0.0.1:8000/asset.html"

import requests

response = requests.post(url, data={
    'k1': valuel,
    'k2': value2
})
print(response.text)
