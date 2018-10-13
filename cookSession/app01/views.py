from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from app01.models import UserInfo


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = UserInfo.objects.filter(user=user, pwd=pwd).first()

        if user:
            # 登陆成功
            '''
            响应体
            return HttpResponse()
            return render()
            return redirect()
            '''
            resporse = HttpResponse("登陆成功！")
            # resporse.set_cookie("is_login", True, max_age=15)
            resporse.set_cookie("is_login", True)
            import datetime
            # date = datetime.datetime(year=2018, month=9, day=26, hour=16, minute=15)
            # resporse.set_cookie("username", user.user, expires=date)
            resporse.set_cookie("username", user.user, path="/index/")
            return resporse

    return render(request, "login.html")


def index(request):
    # 获取cookie
    print("index:", request.COOKIES)
    is_login = request.COOKIES.get("is_login")
    if is_login:
        username = request.COOKIES.get("username")
        import datetime
        now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        last_time = request.COOKIES.get("last_visit_time", "")
        response = render(request, "index.html", {"username": username, "last_time": last_time})
        response.set_cookie("last_visit_time", now)
        return response
    else:
        return redirect("/login/")


def test(request):
    print("test:", request.COOKIES)
    return HttpResponse("test!")


def login_session(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        user = UserInfo.objects.filter(user=user, pwd=pwd).first()

        if user:
            import datetime

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session["is_login"] = True
            request.session["username"] = user.user
            request.session["last_visit_time"] = now

            '''
            1 生成随机字符串   23435643563
            2 response.set_cookie("sessionid",123234234)
            3 在django-session表中创建一条记录：
               session-key     session-date
               234234fdkgljstd   {"is_login":True,"usernmae":"yuan"} 
            '''
            return HttpResponse("登录成功！")
    return render(request, "login.html")


def index_session(request):

    print("is_login:", request.session.get("is_login"))
    '''
    1 request.COOKIE.get("session")  #  sdljkflksdjflsjdflksdjf
    2 django-session表中过滤记录：
        在django-session表中创建一条记录：
            session-key         session-data
            lksjdflksjdfkljsdlfkjsdlfjsldfjksdjflk   {"is_login":True,"user"}
    3 obj.session-data.get("is_login")
    '''
    is_login = request.session.get("is_login")
    if not is_login:
        return redirect("/login_session")

    username = request.session.get("username")
    last_visit_time = request.session.get("last_visit_time")

    return render(request, "index.html", {"username": username, "last_visit_time": last_visit_time})


def logout(request):
    # del request.session["is_login"]
    # request.session.flush()
    auth.logout(request)
    '''
    1 randon_str=request.COOKIE.get("sessionid")
    2 django-session.objects.filter(session-key=randon_str).delete()
    3 response.delete_cookie("sessionid",)
    '''
    return redirect("/login/")

