#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author ：layman
@Date   ：2021/2/10 12:44
@Desc   ：
'''
import json
import csv

# 需求json中的数据转化为csv
# 分别读取创建文件
json_fp = open('33new.json', 'r', encoding='utf-8')
csv_fp = open('34_csv.csv', 'w', encoding='utf-8')

# 提出表头,表内容
data_list = json.load(json_fp)
# sheet_title = data_list[0].keys()
sheet_title = {"姓名", "年龄"}
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())
# csv写入器
writer = csv.writer(csv_fp)
# 写入表头
writer.writerow(sheet_title)
# 写入内容
writer.writerows(sheet_data)
# 关闭两个文件
csv_fp.close()
json_fp.close()
