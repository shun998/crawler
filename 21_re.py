#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 13:37
@Desc   ：
'''
# import requests
#
# r = requests.get("https://api.github.com/user", auth=('user', 'pass'))
# print(r.json())
import re

# 贪婪模式 从头匹配到结尾
one = 'mhjdasdknsahd2342432ahkdn'
# 默认贪婪模式
# pattern = re.compile('m(.*)n')  # ['hjdasdksahd2342432ahkd']
pattern = re.compile('m(.*?)n')  # ['hjdasdk']
result = pattern.findall(one)
print(result)
