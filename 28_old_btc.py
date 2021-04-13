#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/9 19:38
@Desc   ：
'''
import requests
from lxml import etree
import json


class BtcSpider(object):
    def __init__(self):
        self.base_url = 'https://www.8btc.com/article/659'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
        self.data_list = []

    # 1.发请求
    def get_response(self, url):
        response = requests.get(url, headers=self.headers)
        # 网页的 编码到底 是 gbk 还是 urf-8  head--meta-charset=""
        # 原因 是 抓取 网页的 编码 就是 gbk的 所以 解码的时候 也是要gbk
        # data = response.content.decode('gbk')
        data = response.content.decode('utf-8')
        return data

    # 2.解析数据
    def parse_data(self, data):
        # 使用xpath 解析当前页面 所有的 新闻title 和url 保存
        # 1.转类型
        xpath_data = etree.HTML(data)

        # 2.根据xpath路径解析
        # 路径 1. 纯手写  2. 借助浏览器的 右击 粘贴xpath路径; 需要修改
        title_list = xpath_data.xpath('//a[@target="_blank"]/text()')
        url_list = xpath_data.xpath('//a[@target="_blank"]/@href')

        for index, title in enumerate(title_list):
            news = {}
            # print(index)
            # print(title)
            news['name'] = title
            news['url'] = url_list[index]
            self.data_list.append(news)

    # 3.保存数据
    def save_data(self):

        # 将 list---str
        data_str = json.dumps(self.data_list)
        with open('28_btc.json', 'w', encoding='utf-8') as f:
            f.write(data_str)

    # 4.启动
    def run(self):

        for i in enumerate([5468, 5460, 1901, 5455, 5380, 5395, 5438]):
            # 1.拼接 完整url
            url = self.base_url + str(i)
            print(url)
            # 2.发请求
            data = self.get_response(url)

            # 3.做解析
            self.parse_data(data)
        # 4.保存
        self.save_data()


BtcSpider().run()
