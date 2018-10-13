#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.5

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print("PATH", environ.get("PATH_INFO"))

    # 当前路径
    path = environ.get("PATH_INFO")

    # 方案1
    # if path == "/favicon.ico":
    #     with open("favicon.ico", "rb") as f:
    #         data = f.read()
    #     return [data]
    # elif path == "/login":
    #     with open("login.html", "rb") as f:
    #         data = f.read()
    #         return [data]
    # elif path == "/index":
    #     with open("index.html", "rb") as f:
    #         data = f.read()
    #         return [data]
    # 方案2

    from urls import url_patterns

    func = None
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break

    if func:
        return [func(environ)]
    else:
        return [b'404!']


httpd = make_server('', 8080, application)

print('Serving HTTP on port 8080...')

# 开始监听HTTP请求：
httpd.serve_forever()
