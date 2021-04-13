#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 13:30
@Desc   ：
'''
import urllib.request


def load_baidu():
    url = "https://www.baidu.com"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    # 创建请求头对象
    request = urllib.request.Request(url, headers=header)
    request.add_header("HH", "hhhhhh")
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    # 响应头
    # print(response.headers)
    request_headers = request.headers
    print(request_headers)
    request_headers = request.get_header("User-agent")
    print(request_headers)
    with open("04_request_handler.html", "w", encoding="utf-8") as f:
        f.write(data)


load_baidu()
