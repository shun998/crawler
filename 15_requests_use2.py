#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 17:44
@Desc   ：
'''
import requests


class RequestSpider:
    def __init__(self):
        url = "http://www.baidu.com"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content
        # 1.获取请求头
        request_headers = self.response.request.headers
        print(request_headers)
        # 2.获取响应头
        response_headers = self.response.headers
        print(response_headers)
        # 3.相应状态码
        response_code = self.response.status_code
        print(response_code)
        # 4.请求cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)
        # 5.响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)


RequestSpider().run()
