# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :Demo04
# @Date     :2020/11/18 10:26 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup

# 构造session对象，登录保持
session = requests.session()
url = "http://el.gengdan.cn/login/index.php"
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'
}
htmlf = session.get(url,headers=headers).text
soup = BeautifulSoup(htmlf,"lxml")

token = soup.find('input',{'name':'logintoken'})
tokenkey = token.get('value')
data = {
    'anchor':'',
    'logintoken':str(tokenkey),
    'username':'180809329',
    'password':'370102200008224913',
    'rememberusername':'1'
}

html = session.post(url,headers=headers,data=data).text
soup1 = BeautifulSoup(html,"lxml")
# alert = soup.find('div',{'class':''})
div_list = soup1.find_all('span', {'class':'media-body'})
for i in div_list:
    print(i.string)
# print(html)
# print(tokenkey)
