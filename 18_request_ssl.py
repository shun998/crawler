#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 12:13
@Desc   ：https是有第三CA证书 但是12306虽然是https但是不是CA证书,他是自己颁布的证书
解决方法:告诉web忽略证书 访问
'''
import requests

url = "https://www.12306.cn/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
response = requests.get(url=url, headers=headers)
data = response.content.decode("utf-8")
with open("18_ssl.html", "w", encoding="utf-8") as f:
    f.write(data)
