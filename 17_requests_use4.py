#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 18:22
@Desc   ：json
'''
import requests
import json

url = "https://api.github.com/user"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
response = requests.get(url, headers=headers)
# data = response.content.decode("utf-8")
# print(data)
# # 上面的类型是str
# data_dict=json.loads(data)
# print(data_dict['message'])
data = response.json()
# json()自动将json字符串转换成为python的dict list
print(data)
print(data['message'])
