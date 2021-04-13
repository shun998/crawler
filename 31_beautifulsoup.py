#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/10 10:28
@Desc   ：
'''
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 转类型,默认bs4调用lxml解析库
soup = BeautifulSoup(html_doc, 'lxml')
# 通用解析方法
# find  返回符合查询条件的第一个标签
result = soup.find(name='a')
result = soup.find(attrs={'class': 'title'})
result = soup.find(text='Tillie')
result = soup.find(
    name='p',
    attrs={'class': 'story'}
)
print(result)
# find_all
result = soup.find_all('a')
result = soup.find_all('a', limit=1)[0]
result = soup.find_all(attrs={'class': 'sister'})
print(result)
# select_one css选择器
result = soup.select_one('.sister')
print(result)
# select css选择器
result = soup.select('.sister')
result = soup.select('head title')
result = soup.select('title,.title')
result = soup.select('a[id="link3"]')
print(result)
# 标签包裹内容 list
result = soup.select('b')[0].get_text()
print(result)
# 标签的属性
result = soup.select('#link1')[0].get('href')
print(result)
