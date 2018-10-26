from django.shortcuts import render, HttpResponse

# Create your views here.


def aseet(request):
    if request.method == 'POST':

        print(request.method)
        return HttpResponse("OK")

