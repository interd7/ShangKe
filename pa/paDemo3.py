# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :paDemo3
# @Date     :2020/10/28 9:48 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import urllib.request
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = urllib.request.urlopen("https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2022165842,3988576039&fm=26&gp=0.jpg")
response = url.read()
# print(response)
with open("baidu.png",'wb') as f:
    f.write(response)
