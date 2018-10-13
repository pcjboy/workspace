#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.6

from django.contrib import admin
from django.urls import path, re_path
from app02 import views

urlpatterns = [
    re_path(r"^index/", views.index, name="index")
]
