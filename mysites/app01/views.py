from django.shortcuts import render, HttpResponse

from django.urls import reverse


# Create your views here.


def timer(request):
    import time
    ctime = time.time()

    # 反解析
    url = reverse("s_c_2003")
    url = reverse("y_a", args=(5555,))

    print(url)

    return render(request, "timer.html", {"date": ctime})


def special_case_2003(request):
    return HttpResponse("special_case_2003")


def year_archive(request, year):
    return HttpResponse(year)


def path_year(request, year):
    print(year)
    print(type(year))

    return HttpResponse("path year.....")


def path_month(request, month):
    print(month, type(month))
    return HttpResponse("path month....")


# def month_archive(request, year, month):
#     return HttpResponse(year+"-"+month)

# 有名分组
def month_archive(request, y, m):
    return HttpResponse(y + "-" + m)


def login(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "login.html")
    else:
        print(request.GET)
        print(request.POST)
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if user == "yuan" and pwd == "123":
            return HttpResponse("登录成功!")
        else:
            return HttpResponse("用户名或者密码错误!")

        return HttpResponse("OK")

    return render(request, "login.html")


def index(request):
    return HttpResponse(reverse("app01:index"))
