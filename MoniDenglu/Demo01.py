# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :Demo01
# @Date     :2020/11/18 8:58 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup as bs4
# 1.通过cookie
url = "http://www.renren.com/275735454/profile"
# # dym0822@163.com  123123123123
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
    'Cookie':'anonymid=kh2rzys3-7w1kwu; _r01_=1; taihe_bi_sdk_uid=2c3057c1890e092311fa2746347caa9d; ln_uact=dym0822@163.com; depovince=BJ; JSESSIONID=abciEbmBOLkcYdadt3yxx; taihe_bi_sdk_session=95cfe6ef3e3c7d8c65773074426400c9; ick_login=7c8c3689-bf31-43c7-b624-6d5718a7b314; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20150711/1725/main_x7Nq_54ba000404d71986.jpg; ick=fd28109e-57ad-4c54-9ed0-4cad5f9c7358; jebecookies=f109478a-65c2-4be4-af41-518434cf205c|||||; _de=B725A4604395D4C35BF7EAB63017E04A; p=2833f0978a0b6b8a852569e4f2a0957d4; ap=275735454; t=2bd714e58304318481155ce6116eecc74; societyguester=2bd714e58304318481155ce6116eecc74; id=275735454; xnsid=26de2654; ver=7.0; loginfrom=null; wp_fold=0'
}

html = requests.get(url,headers=headers).text
soup = bs4(html,"lxml")
name = soup.find("title")
print(name)
# 2.通过表单请求
# url = "http://www.renren.com/PLogin.do"
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69',
# }
# data = {'email':'dym0822@163.com',
#         'password':'123123123123'
#         }
# html = requests.get(url,headers=headers,data=data).text
# print(html)
