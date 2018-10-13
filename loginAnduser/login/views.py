from django.shortcuts import render, HttpResponse, redirect

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
    pass
    return render(request, 'classess.html')