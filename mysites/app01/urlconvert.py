#!/usr/bin/env pythony
# _*_coding:utf-8_*_
# __author__ = pcjboy
# Date 18.9.6


class MonConvert:
    regex = "[0-9]{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):  # 反向解析
        return '%04d' % value
