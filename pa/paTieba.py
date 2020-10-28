# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :paTieba
# @Date     :2020/10/28 10:54 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
import time
start_time = time.time()
# ===============贴吧翻页================
name = input("请输入您要访问的贴吧:")
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

for i in range(1,11):
    page = 50*(i-1)
    url = "https://tieba.baidu.com/f?kw={0}&ie=utf-8&pn={1}".format(name,page)
    print(url)

    response = requests.get(url,headers=headers).content.decode("utf-8")
    with open("{}吧第{}页.html".format(name,i),"w",encoding="utf-8")as fp:
        fp.write(response)

end_time = time.time()
sum_time = end_time - start_time
print("花费时间",sum_time)
