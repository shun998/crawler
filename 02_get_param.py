#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 12:23
@Desc   ：
'''
import urllib.request
import urllib.parse
import string


def get_method_param():
    url = "http://www.baidu.com/s?wd="
    # 拼接字符串
    name = "美女"
    # 将含有汉字的网址转译
    final_url = url + name
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    # 使用代码发送网络请求
    response = urllib.request.urlopen(encode_new_url)
    data = response.read().decode("utf-8")
    print(data)
    # 保存到本地
    with open("02_encode.html", "w", encoding="utf-8") as f:
        f.write(data)
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11:
    # ordinal not in range(128)
    # python是解释型语言:解析器只支持ASCII 0-127


get_method_param()
