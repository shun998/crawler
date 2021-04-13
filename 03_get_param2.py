#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 12:51
@Desc   ：
'''
import urllib.request
import urllib.parse
import string


def get_params():
    url = "http://www.baidu.com/s?"
    params = {"wd": "中文", "key": "zhang", "value": "san"}
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)
    print(final_url)


get_params()
