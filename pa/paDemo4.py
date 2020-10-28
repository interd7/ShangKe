# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :paDemo4
# @Date     :2020/10/28 10:37 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
kw = input('请输入要查询的课程名称: ')
url = "https://www.imooc.com/search/?type=course&words={}".format(kw)
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
response = requests.get(url=url,headers=headers).content.decode("UTF-8")

with open("course.html",'w',encoding="utf-8")as fp:
    fp.write(response)
