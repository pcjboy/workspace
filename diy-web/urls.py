#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.5

from views import *

url_patterns = [
    ("/login", login),
    ("/index", index),
    ("/reg", reg),
    ("/favicon", favicon),
    ("/timer", timer),
    ("/auth", auth),
]