#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 14:53
@Desc   ：
'''
import urllib.request


def create_proxy_handler():
    url = "https://blog.csdn.net/lzf601/article/details/106068866/"
    # 添加代理
    proxy = {
        # 免费的写法
        # "http": "http://140.207.229.171:80"
        # "http": "140.207.229.171:80"
        # 付费代理的写法
                "http":"xiaoming@1123231"
    }
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    data = opener.open(url).read()
    print(data)


create_proxy_handler()
