#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/9 15:43
@Desc   ：
'''
import re
import requests

url = 'http://news.baidu.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
data = requests.get(url, headers=headers).content.decode('utf-8')
# 正则解析新闻 每个新闻的title url
# /html/body/div[3]/div[2]/div[1]/div/div[3]/div[1]/div/ul/li[2]/strong/a[2]
# //*[@id="pane-news"]/div/ul/li[2]/strong/a[2]
# pane-news > div > ul > li.hdline1 > strong > a:nth-child(3)
# <a href="https://wap.peopleapp.com/article/6132283/6039672"  mon="r=1"><b>总书记牵挂的民生事</b></a>
# pattern = re.compile('<a href="(.*?)" target="_blank" mon="(.*?)">(.*?)</a>')
pattern = re.compile('<a (.*?)</a>',re.S)
result = pattern.findall(data)
print(result)
with open('25_news.html', 'w', encoding='utf-8')as f:
    f.write(data)
