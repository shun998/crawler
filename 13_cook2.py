#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 16:33
@Desc   ：获取个人中心
代码登录 登录成功 cookie(有效)
自动带着cookie去请求个人中心
'''
import urllib.request
from http import cookiejar
import urllib.parse
import string

# cookiejar可以自动保存cookie
# 1.代码登录
# 1.1 登录的网址
# 1.2 登录的参数
# 1.3 发送网络请求
login_url = "https://www.yaozh.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
login_form_data = {
    "type": "0",
    "username": "shun998",
    "pwd": "dsgzs0818",
    "country": "86_zh-CN",
    "formhash": "702061E93D",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"

}
cookie_jar = cookiejar.CookieJar()
# 定义有添加 cookie 功能的处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
# 处理器生产open
opener = urllib.request.build_opener(cookie_handler)
# 带着参数post请求
login_str = urllib.parse.urlencode(login_form_data, safe=string.printable).encode("utf-8")
login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
# 如果登录成功,cookiejar自动保存cookie
opener.open(login_request)
# 2.带着cookie去访问个人中心
center_url = "https://www.yaozh.com/member/"
center_request = urllib.request.Request(center_url, headers=headers)
response = opener.open(center_url)
data = response.read().decode("utf-8")
with open("13_cookie.html", "w", encoding="utf-8") as f:
    f.write(data)
