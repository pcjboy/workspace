from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    return render(request, "index.html")


def test_ajax(request):
    print(request.GET)

    return HttpResponse("hello yuan")


def cal(request):
    print(request.POST)

    n1 = int(request.POST.get("n1"))
    n2 = int(request.POST.get("n2"))
    ret = n1 + n2

    return HttpResponse(ret)


from app01.models import User


def login(request):
    print(request.POST)
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    user = User.objects.filter(name=user, pwd=pwd).first()

    res = {"user": None, "msg": None}
    if user:
        res["user"] = user.name
        print(user.name, user.pwd)
    else:
        res["msg"] = "username or password wrong!"

    import json
    print(json.dumps(res))
    return HttpResponse(json.dumps(res))


def file_put(request):
    if request.method == "POST":
        print("body", request.body)  # 请救济报文中的请求体
        print("POST", request.POST)  # if contentType==urlencoded, request.POST

        print(request.FILES)
        #
        # file_obj = request.FILES.get("avatar")
        # with open(file_obj.name, "wb") as f:
        #     for line in file_obj:
        #         f.write(line)

        return HttpResponse("OK")

    return render(request, "file_put.html")
