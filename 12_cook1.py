#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/5 16:17
@Desc   ：直接粘贴 个人中心的页面
手动粘贴 复制 PC抓包cookies
放在request请求头
'''
import urllib.request

url = "https://www.yaozh.com/member/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Cookie": "acw_tc=2f624a6416125130953296374e1e9b4acabaf522d1b9294a2eeb1e4238ce25; PHPSESSID=ofp9jckr5q4eu0gop3tla9c6o0; _ga=GA1.2.487724492.1612513094; _gid=GA1.2.1064044487.1612513094; think_language=zh-CN; yaozh_logintime=1612513671; yaozh_user=1041200%09shun998; yaozh_userId=1041200; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyYnoaSZ5lml5SVg26qb21rg66flM6bh5%2BscZhyVNbN18%2BdnZlZoKifnZ%2BDn5iorJDVop6Yg3HYnmpnm1pjmZa87337e05f143689946d65D977D303eDDUlpWXl26VV6DXn5VtWamhnsZbbKabZ5ieW2iXaWSYlpWXm5eVb5dXoOE%3Da803dc453c73bc3c7d092ecfffdd3b27; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1612513672; yaozh_uidhas=1; yaozh_mylogin=1612513678; acw_tc=2f624a6416125130953296374e1e9b4acabaf522d1b9294a2eeb1e4238ce25; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1612513094%2C1612513610"}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
data = response.read().decode("utf-8")
# 保存文件
with open("12_cook.html", "w", encoding="utf-8") as f:
    f.write(data)
