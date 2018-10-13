from django.shortcuts import render
from django.shortcuts import HttpResponse

'''
http://127.0.0.1:8000/index/?name=rewrt&age=ert
url: 协议://ip:port/路径?get请求数据
'''

# Create your views here.
def index(request):

    print("method", request.method)

    print(request.GET)
    print(request.GET.get("name"))
    print(request.POST)

    print(request.path)
    return render(request, "index.html")
