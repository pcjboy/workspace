"""mysites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, register_converter
from app01 import views

from app01.urlconvert import MonConvert

# 注册自定义转换器
register_converter(MonConvert, "mm")

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('timer/', views.timer),
    # # 反解析
    # path('login/', views.login, name="Log"),

    # re_path(r'^articles/2003/$', views.special_case_2003),
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    # # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # # 有名分组
    # re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$', views.month_archive),

    # 分发:

    # re_path(r"^app01/", include("app01.urls")),
    # re_path(r"^app02/", include("app02.urls")),

    # 命名空间
    # re_path(r"^app01/", include(("app01.urls", "app01"))),
    # re_path(r"^app02/", include(("app02.urls", "app02"))),
    # re_path(r"^", include("app01.urls")),

    # path("articles/<path:year>", views.path_year),
    path("articles/<mm:month>", views.path_month)


]
