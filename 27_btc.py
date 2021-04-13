#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/9 17:41
@Desc   ：
'''
import json

import requests
from lxml import etree
import re


class BtcSpider:
    def __init__(self):
        self.base_url = 'https://www.8btc.com/article/659'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
        # 发请求
        self.data_list = []

    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        data_list = response.content.decode('utf-8')
        return data_list
        # 解析数据

    def parse_data(self):
        xpath_data = etree.HTML(self.data_list)

        for index, title in enumerate(title_list):
            news = {}
            news['name'] = title
            news['url'] = url_list[index]
            self.data_list.append(news)

    # 保存数据
    def save_data(self):
        # 将list转化为json字符串
        data_str = json.dumps(self.data_list)
        with open('27_btc.json', 'w', encoding='utf-8')as f:
            f.write(data_str)
        # 启动

    def run(self):
        # 拼接完整url
        for i in range(4000, 4004):
            url = self.base_url + str(i)
            print(url)
            # 发请求
            data = self.get_response(url)
            # 做解析
            parse_data = self.parse_data(data)
            # 保存
        self.save_data()


BtcSpider().run()
