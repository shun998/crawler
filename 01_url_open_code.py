#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 10:22
@Desc   ：
'''
import urllib.request


def load_data():
    url = "http://www.baidu.com/"  # s提取的内容少很多
    # get请求
    # response :http相应的对象
    response = urllib.request.urlopen(url)
    # print(response)
    # <http.client.HTTPResponse object at 0x000001EE0B2A2C10>
    data = response.read()
    print(data)
    str_data = data.decode("utf-8")
    print(str_data)
    # 将数据持久化
    with open("01_url_code.html", "w", encoding="utf-8") as f:
        f.write(str_data)
    # 将字符串转化为bytes
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")
    print(bytes_name)
    # python爬取的类型:str bytes
    # 如果爬取出来的是bytes类型,但是写入的时候需要str decode("utf-8")
    # 如果爬取出来的是str类型,但是写入的时候需要bytes encode("utf-8")


load_data()
