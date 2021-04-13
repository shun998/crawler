#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 15:43
@Desc   ：付费代理,通过验证的处理器发送
'''
import urllib.request
import requests


def money_proxy_use():
    # 第一种
    # 代理ip
    money_proxy = {"http": "username:pwd@192.168.12.1:8080"}
    # 代理的处理器
    handler = urllib.request.ProxyHandler(money_proxy)
    # 通过处理器创建opener
    opener = urllib.request.build_opener(handler)
    # open发送请求
    opener.open("http://www.baidu.com")
    # 第二种
    user_name = "abcname"
    pwd = "123456"
    proxy_money = "123.158.63.130:8888"
    # 创建密码管理器,添加用户名和密码
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, proxy_money, user_name, pwd)
    # 创建可以验证的ip处理器
    handler_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
    # 创建opener
    opener_auth = urllib.request.build_opener(handler_auth_proxy)
    # 发送请求
    response = opener_auth.open("http://www.baidu.com")
    print(response.read())
    # 爬取自己公司的数据,做数据分析
    #admin

money_proxy_use()
