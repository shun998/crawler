#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 17:04
@Desc   ：
'''
import re

one = """
mssfajisfajkpoafn
1234465789N
"""
# . 不能匹配换行
pattern = re.compile('m(.*)n', re.S | re.I)
result = pattern.findall(one)
print(result)
