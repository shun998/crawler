#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/6 12:21
@Desc   ：
'''
import requests

# 请求url
member_url = "https://www.yaozh.com/member/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
# cookies的字符串
cookies = "acw_tc=707c9fd616125852992168622e7bf2d05804f18dfb73449fbf099ecac40b8b; PHPSESSID=mdbtfuiii5uredlc1ico68ef95; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1612585295; _ga=GA1.2.1952525176.1612585295; _gid=GA1.2.341521902.1612585295; yaozh_logintime=1612585481; yaozh_user=1041200%09shun998; yaozh_userId=1041200; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyYnoaSZ5lml5SVg26qb21rg66flM6bh5%2BscZhyVNbN18%2BdnZlZoKifnZ%2BDn5iorJDVop6Yg3HYnmpnm1pjmZa4a85834AD9C8A37c4760c3d2Cc299424UlpWblWqWV6DXn5VtWamhnsZbbKabZ5ieW2iXaWSYnZeVnJaZbJlXoOE%3D97899eadfb1ac6fa782f33f70a54420e; db_w_auth=856099%09shun998; UtzD_f52b_saltkey=Nc6MIhdr; UtzD_f52b_lastvisit=1612581882; UtzD_f52b_lastact=1612585482%09uc.php%09; UtzD_f52b_auth=c6cbqoy8k%2F4M9i3e94ejCnUPRbZUSn4fRh1zI0bK50Sy7vzNcP1neYXMMItrx4B3polE%2BX5V%2F0r41pxyRWcxFnTvVfM; yaozh_uidhas=1; yaozh_mylogin=1612585484; acw_tc=707c9fd616125852992168622e7bf2d05804f18dfb73449fbf099ecac40b8b; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1612513094%2C1612513610%2C1612585295"
# cookie_dict = {
#     "acw_tc": "707c9fd616125852992168622e7bf2d05804f18dfb73449fbf099ecac40b8b",
#     "PHPSESSID": "mdbtfuiii5uredlc1ico68ef95",
#     "Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94": "1612585295",
#     "_ga": "GA1.2.1952525176.1612585295",
#     "_gid": "GA1.2.341521902.1612585295",
#     "yaozh_logintime": "1612585481",
#     "yaozh_user": "1041200%09shun998",
#     "yaozh_userId": "1041200",
#     "yaozh_jobstatus": "kptta67UcJieW6zKnFSe2JyYnoaSZ5lml5SVg26qb21rg66flM6bh5%2BscZhyVNbN18%2BdnZlZoKifnZ%2BDn5iorJDVop6Yg3HYnmpnm1pjmZa4a85834AD9C8A37c4760c3d2Cc299424UlpWblWqWV6DXn5VtWamhnsZbbKabZ5ieW2iXaWSYnZeVnJaZbJlXoOE%3D97899eadfb1ac6fa782f33f70a54420e",
#     "db_w_auth": "856099%09shun998",
#     "UtzD_f52b_saltkey": "Nc6MIhdr",
#     "UtzD_f52b_lastvisit": "1612581882",
#     "UtzD_f52b_lastact": "1612585482%09uc.php%09",
#     "UtzD_f52b_auth": "c6cbqoy8k%2F4M9i3e94ejCnUPRbZUSn4fRh1zI0bK50Sy7vzNcP1neYXMMItrx4B3polE%2BX5V%2F0r41pxyRWcxFnTvVfM",
#     "yaozh_uidhas": "1",
#     "yaozh_mylogin": "1612585484",
#     "acw_tc": "707c9fd616125852992168622e7bf2d05804f18dfb73449fbf099ecac40b8b",
#     "Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94": "1612513094%2C1612513610%2C1612585295"
# }
# 上面的方式比较复杂,每次使用都需要使用正则
# 此时需要传递的是cookies的cookiejar或者dict类型数据
cookie_dict = {}
cookie_list = cookies.split(";")
for cookie in cookie_list:
    cookie_dict[cookie.split("=")[0]] = cookie.split("=")[1]
# 上面的字典推导式
cookie_dict = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies.split(";")}
response = requests.get(member_url, headers=headers, cookies=cookie_dict)
data = response.content.decode("utf-8")
with open("19_member2.html", "w", encoding="utf-8") as f:
    f.write(data)
