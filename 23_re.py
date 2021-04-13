#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 17:10
@Desc   ：
'''
import re

# 纯数字的正则
pattern = re.compile('^\d+$')
one = '123'
# result = pattern.findall(one) # ['1', '2', '3']
# match 从头开始匹配,匹配一次,返回第一个
result = pattern.match(one)
print(result.group())
