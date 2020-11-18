# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :Demo02
# @Date     :2020/11/18 9:10 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup as bs
url = "http://el.gengdan.cn/my/"
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Cookie':'MoodleSession=cb9d94cb10fa8b8dd5eccec0cfa329bb; MOODLEID1_=%25A44W%2521%25EF%25FF%2517%253Fo'
}

html = requests.get(url,headers=headers).text
# print(html)
soup = bs(html,"lxml")
div_list = soup.find_all('span', {'class':'media-body'})
for i in div_list:
    print(i.string)
