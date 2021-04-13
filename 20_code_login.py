#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 12:48
@Desc   ：
'''
import requests

member_url = "https://www.yaozh.com/member/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
# 自动保存cookie,相当于cookiejar
session = requests.session()
# 代码登录
login_url = "https://www.yaozh.com/login/"
login_form_data = {
    "type": "0",
    "username": "shun998",
    "pwd": "dsgzs0818",
    "country": "86_zh-CN",
    "formhash": "9B91A0E9D6",
    "backurl": "https%3A%2F%2Fwww.yaozh.com%2F"
}
login_response = session.post(login_url, data=login_form_data, headers=headers)
data = session.get(member_url, headers=headers).content.decode("utf-8")
with open("20_code.html", "w", encoding="utf-8") as f:
    f.write(data)
