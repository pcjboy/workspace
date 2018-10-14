from django.shortcuts import render, HttpResponse, redirect
import pymysql


# Create your views here.


def index(request):
    pass
    return render(request, "index.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html", {'msg': '123123'})
    else:
        # print(request.POST)
        u = request.POST.get("username")
        p = request.POST.get("password")
        if u == "root" and p == '123123':
            # 登陆成功
            return redirect('http://www.baidu.com')
        else:
            # 登录失败
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


def classes(request):
    conn = pymysql.connect(host='10.21.10.58', port=3306, user='loginuser', passwd='loginuser', db='loginuser',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, title from login_classtable")
    class_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'classess.html', {'class_list': class_list})


def add_class(request):

    return render(request, "add_class.html")
