# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1007(2)
# @Date     :2020/10/7 11:58 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# -*- coding: utf-8 -*-
# import openpyxl
# import random
#
# myList = []
# #  1. 读取excel文档
# wb = openpyxl.load_workbook(r'/Users/fushengyuanwuhui/Downloads/计科18级学生名单.xlsx')
# #  2. 获取工作表中
# sheet = wb[wb.sheetnames[0]]
# for row in sheet.rows:
#     list1 = []
#     for cell in row:
#         list1.append(cell.value)
#     myList.append(list1)
#
# set1 = set()
# while True:
#     c1 = random.randint(1, 80)
#     set1.add(c1)
#     if (len(set1) == 20):
#         break
#
# k = 0
# for j in set1:
#     print(myList[j],end="\t")
#     k += 1
#     if (k == 5):
#         print()
#         k = 0

import requests
import parsel
import os
import time
from urllib import parse
# 请求头与网址
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
url = 'https://www.vmgirls.com/13344.html'
# 请求网页
response = requests.get(url=url, headers=headers)
html = response.text
# 解析网页
pars = parsel.Selector(html)
data_list = pars.xpath('//div[@class="nc-light-gallery"]/p/a/@href').getall()
# 获取文件夹名
dir_name = pars.xpath('//div[@class="nc-light-gallery"]/p/a/img/@alt').get()
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# 保存图片
for img in data_list:
    # 加一秒延迟
    time.sleep(1)
    # 相对路径转为绝对路径
    img_url = parse.urljoin('http://www.vmgirls.com/', img)
    data = requests.get(url=img_url, headers=headers).content
    # 获取图片名
    file_name = img_url.split('/')[-1]
    with open(dir_name + '/' + file_name, mode='wb') as f:
        f.write(data)
        print('正在保存', file_name)

