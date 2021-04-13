#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 16:03
@Desc   ：
'''
import urllib.request


def auth_neiwang():
    # 用户名 密码
    user = "admin"
    pwd = "admin123"
    nei_url = "http://192.168.179.55"
    # 创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwd_manager.add_password(None, nei_url, user, pwd)
    # 创建认证的管理器(requests)
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)
    auth_opener = urllib.request.build_opener(auth_handler)
    response = auth_opener.open(nei_url)
    print(response)


auth_neiwang()
