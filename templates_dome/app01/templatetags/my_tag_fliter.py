#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.6

from django import template

register = template.Library()


@register.filter
def multi_fliter(x, y):
    return x * y


@register.simple_tag
def multi_tag(x, y):
    return x * y
