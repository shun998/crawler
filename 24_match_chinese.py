#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 17:20
@Desc   ：
'''
import re

# 拆分字符串
one = 'asbsosos'
pattern = re.compile('s')
result = pattern.split(one)
print(result)
# 匹配中文
two = '2月5日20时，“天问一号”探测器发动机点火工作，顺利完成地火转移段第四次轨道中途修正，以确保按计划实施火星捕获。'

pattern = re.compile('[\u4E00-\u9FA5]')
result = pattern.findall(two)
print(result)
