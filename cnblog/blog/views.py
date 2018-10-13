from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.http import JsonResponse
from django.contrib import auth
from blog.myfoms import UserForm
from blog.models import UserInfo


def login(request):
    if request.method == "POST":
        response = {"user": None, "msg": None}
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        valid_code = request.POST.get("valid_code")

        valid_code_str = request.session.get("valid_code_str")
        if valid_code == valid_code_str:
            user = auth.authenticate(username=user, password=pwd)
            if user:
                auth.login(request, user)  # request.user == 当前登陆对象
                response["user"] = user.username
            else:
                response["msg"] = "username or password error!"
        else:
            response["msg"] = "valid code error!"
        return JsonResponse(response)
    return render(request, "login.html")


def get_validCode_img(request):
    """
    基于PIL模块动态生成响应状态码图片
    :param request:
    :return:
    """
    from blog.utils.validCode import get_valid_code_img
    data = get_valid_code_img(request)
    return HttpResponse(data)


def index(request):
    return render(request, "index.html")


def register(request):
    if request.is_ajax():
        print(request.POST)
        form = UserForm(request.POST)

        response = {"user": None, "msg": None}
        if form.is_valid():
            response["user"] = form.cleaned_data.get("user")

            # 生成一条用户纪录
            user = form.cleaned_data.get("user")
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")
            request.FILES.get("avatar")
            UserInfo.objects.create_user(username=user, password=pwd, email=email)
        else:
            print(form.cleaned_data)
            print(form.errors)
            response["msg"] = form.errors
        return JsonResponse(response)
    form = UserForm()
    return render(request, "register.html", {"form": form})
