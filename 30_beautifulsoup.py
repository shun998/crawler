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
# 解析数据
# Tag
result = soup.head
result = soup.p
result = soup.a
print(type(result))  # <class 'bs4.element.Tag'>
result = soup.a.string
print(type(result))  # <class 'bs4.element.NavigableString'>
result = soup.a['href']
print(type(result))  # <class 'str'>
print(type(soup))  # <class 'bs4.BeautifulSoup'>
