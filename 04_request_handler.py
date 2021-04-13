#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 13:30
@Desc   ：
'''
import urllib.request


def load_baidu():
    url = "http://www.baidu.com"
    # 创建请求头对象
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data=response.read().decode("utf-8")
    # 响应头
    # print(response.headers)
    request_headers = request.headers
    print(request_headers)
    with open("04_request_handler.html","w",encoding="utf-8") as f:
        f.write(data)


load_baidu()
