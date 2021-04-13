#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/9 16:25
@Desc   ：
'''
import re
from lxml import etree

import requests

url = 'http://news.baidu.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
data = requests.get(url, headers=headers).content.decode('utf-8')
# 转解析类型
xpath_data = etree.HTML(data)
# 调用xpath的方法
result = xpath_data.xpath('/html/head/title/text()')
result = xpath_data.xpath('//a/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=1"]/text()')
result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=1"]/@href')
result = xpath_data.xpath('//li/a/text()')
print(result)
# with open('25_news.html', 'w', encoding='utf-8')as f:
#     f.write(data)
