# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :paDemo2
# @Date     :2020/10/28 9:32 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
# 1.找到图片url
url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
url1 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1594613469334&di=ed17b6b6f0f26e775fa3b9953d0f7055&imgtype=0&src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_bt%2F0%2F6294450852%2F1000'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

# 2.发起请求：
response = requests.get(url=url1,headers=headers).content
with open('houzi.png','wb')as fp:
    fp.write(response)
