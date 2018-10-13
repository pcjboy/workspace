#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.5

# 生成用户表

import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='divweb', passwd='web', db='divweb')
# 创建游标
cur = conn.cursor()

sql = '''
create table userinfo(
        id INT primary key ,
        name VARCHAR(32),
        password VARCHAR(32)
)
'''

cur.execute(sql)

# 提交
conn.commit()
# 关闭指针对象
cur.close()

'''
WEB 框架 功能总结
main.py： 启动文件， 封装了socket

1 urls.py: 路径与视图函数映射关系           ---- url 控制器
2 views.py 视图函数，固定有一个形式参数： environ  -------视图函数
3 templates 文件夹： html文件                     ------模板
4 models: 在项目启动前， 在数据库中创建表结构    ------ 与数据库相关

'''