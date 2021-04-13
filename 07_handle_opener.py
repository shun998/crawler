#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 14:36
@Desc   ：
'''
import urllib.request


def opener():
    # 系统的urlopen并没有添加代理功能,所以需要自定义这个功能
    # urllib.request.urlopen()
    # ssl是第三方的CA证书
    # http 8080 https 443
    # urlopen可以请求数据 handler
    url = "https://blog.csdn.net/lzf601/article/details/106068866/"
    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的opener
    opener = urllib.request.build_opener(handler)
    # 用自己创建的opener请求数据
    response = opener.open(url)
    data = response.read().decode("utf-8")
    print(response)
    print(data)
    with open("07-csdn.html", "w", encoding="utf-8") as f:
        f.write(data)


opener()
