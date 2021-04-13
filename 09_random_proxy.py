#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 15:04
@Desc   ：
'''
import urllib.request


def proxy_user():
    proxy_list = [
        {"http": "121.232.148.139:9000"},
        {"http": "113.194.128.171:9999"},
        {"http": "123.54.52.83:9999"},
        {"http": "175.42.123.52:9999"},
        {"http": "113.194.137.189:9999"}
    ]
    for proxy in proxy_list:
        print(proxy)
        # 利用遍历出的ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        # 创建opener
        opener = urllib.request.build_opener(proxy_handler)
        try:
            opener.open("http://www.baidu.com", timeout=1)
            print("hhh")
        except Exception as e:
            print(e)


proxy_user()
