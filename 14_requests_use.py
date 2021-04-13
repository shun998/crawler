#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 17:44
@Desc   ：
'''
import requests

url = "http://www.baidu.com"
response = requests.get(url)
# content返回的属性是字节
# text 返回字符串,优先使用content.text可能会编码不正确
data = response.content.decode("utf-8")
print(data)
