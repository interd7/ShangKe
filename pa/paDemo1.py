# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :paDemo1
# @Date     :2020/10/28 9:11 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import urllib.request
# response = urllib.request.urlopen("https://www.baidu.com")
# html = response.read().decode('UTF-8')
urllib.request.urlretrieve("http://www.sohu.com","sohu.html")
# print(response.info())
# print(response.geturl())
# print(response.getcode())
# with open('yimai7.html','w',encoding='utf-8')as fp:
#     fp.write(html)
