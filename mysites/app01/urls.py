#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.6

from django.contrib import admin
from django.urls import path, re_path, include

from app01 import views

urlpatterns = [

    # re_path(r'^articles/2003/$', views.special_case_2003, name="s_c_2003"),
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive, name="y_a"),
    # # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # # 有名分组
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive),
    # re_path("^index/", views.index, name="index")
]
