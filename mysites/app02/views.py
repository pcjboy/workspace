from django.shortcuts import render, HttpResponse

# Create your views here.
from django.urls import reverse


def index(requset):
    return HttpResponse(reverse("app02:index"))
