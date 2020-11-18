# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :Demo03
# @Date     :2020/11/18 10:17 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# 1
import time

import requests
import pytesseract
from bs4 import BeautifulSoup
from PIL import Image
from school_api.check_code import CHECK_CODE
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
}


url = 'http://jw.gengdan.cn/(txxd55jdlsd3y055525aye45)/default2.aspx'
url_checkcode = 'http://jw.gengdan.cn/(txxd55jdlsd3y055525aye45)/CheckCode.aspx'
# url_xuefen = "http://jw.gengdan.cn/(ivtfkp45jtlnfgujt4wnsnat)/xscjcx.aspx?xh=180809334&xm=%C0%EE%BF%C6%EC%BE&gnmkdm=N121605"

S = requests.session()
#此处写session是为了避免与登陆成功后的session不一致导致的401错误


# 获取登录数据的函数  url为登录页面
def get_post_data(url):
    html = S.get(url)
    # html_xuefen = S.get(url_xuefen)
    # soup1 = BeautifulSoup(html_xuefen.text,'lxml')

    soup = BeautifulSoup(html.text, 'lxml')
    viewState = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    # viewState_xuefen = soup1.find('input', attrs={'name': '__VIEWSTATE'})['value']

    # cookies = requests.utils.dict_from_cookiejar(S.cookies)
    # print(cookies)
    # 把cookie转变成字典类型

    # headers.update(cookies)

    # 获取验证码，下载到本地

    code = S.get(url_checkcode, headers=headers)
    check_result = CHECK_CODE.verify(code.content)
    with open("code.gif", "wb") as f:
        f.write(code.content)
        print(check_result)

    # 打开验证码图片
    image = Image.open('code.gif')
    image.show()




    user = input("学号:")
    pwd = input("密码:")
    checkCode = input("验证码:")
    print("正在登录。。。")
    time.sleep(1)
    print("欢迎你：")


    # post的登录数据
    login_info = {
        "__VIEWSTATE": viewState,
        'txtUserName': user,
        'Textbox1': '',
        'TextBox2': pwd,
        'txtSecretCode': checkCode,
        "RadioButtonList1": "%D1%A7%C9%FA",
        "Button1": "",
        "lbLanguage": ""
    }
    # login_xuefen = {
    #     "__VIEWSTATE": viewState_xuefen,
    #     'Button1': '%B3%C9%BC%A8%CD%B3%BC%C6'
    # }
    return login_info

def judge(html):
    soup_judge = BeautifulSoup(html, 'html.parser')
    script = soup_judge.find_all('script')[0].text
    # print(script)
    # print(soup_judge)
    if "验证码不正确" in script:
        return "验证码错误"
    elif "用户名不存在" in script:
        return "用户名不存在"
    elif "密码错误" in script:
        return "密码错误"
    else:
        return 1

def login(url, data):
    req = S.post(url=url, data=data, headers=headers)
    # print(req.text)


    # 判断登录数据是否正确 如果正确输出绩点（以绩点为例），如果错误 显示错误类型 并重新执行程序
    if judge(req.text) == 1:
        content_req = S.get("http://jw.gengdan.cn/(txxd55jdlsd3y055525aye45)/xs_main.aspx?xh=180809329")
        soup2 = BeautifulSoup(content_req.text, 'lxml')
        score = soup2.find('span', attrs={'id': 'xhxm'})
        #查询课表
        # content_class = S.get("http://jw.gengdan.cn/(txxd55jdlsd3y055525aye45)/xscjcx.aspx?xh=180809329&xm=%C0%EE%BF%C6%EC%BE&gnmkdm=N121605")
        # soup3 = BeautifulSoup(content_class.text,'lxml')
        # score_class = soup3.find('span', attrs={'id': 'pjxfjd'})
        # print("登录成功！")
        time.sleep(1)
        print(score.text)
        # time.sleep(1)
        # print(score_class)
    else:
        print("登陆失败")
        # main()


def main():
    data = get_post_data(url)
    login(url, data)


if __name__ == '__main__':
    main()


# 2
# import requests
#
# import os
# # 这是Python的一个非常有名的图片库，这里我们用它来显示验证码
# from PIL import Image
# from bs4 import BeautifulSoup
#
#
# def get_post_data(url):
#     # 首先获取到登录界面的html
#     html = requests.get(url)
#
#     soup = BeautifulSoup(html.text, 'lxml')
#     # print(soup)
#
#     # 找到form的验证参数
#     __VIEWSTATE = soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
#
#     # 下载验证码图片
#     pic = requests.get(
#         'http://jw.gengdan.cn/(ivtfkp45jtlnfgujt4wnsnat)/CheckCode.aspx').content
#     with open('ver_pic.png', 'wb') as f:
#         f.write(pic)
#
#     # 打开验证码图片
#     image = Image.open('{}/ver_pic.png'.format(os.getcwd()))
#     image.show()
#
#     # 构造需要post的参数表
#     data = {'__VIEWSTATE': '',
#             '__VIEWSTATEGENERATOR': '92719903',
#             'txtUserName': '',
#             'Textbox1': '',
#             'TextBox2': '',
#             'txtSecretCode': "",
#             # 这里我将radio栏--学生 encode成gbk编码，以符合数据的要求
#             'RadioButtonList1': "%D1%A7%C9%FA",
#             }
#
#     # 构造登录的post参数
#     data['__VIEWSTATE'] = __VIEWSTATE
#     data['txtSecretCode'] = input('请输入图片中的验证码:')
#     data['txtUserName'] = input("请输入学号:")
#     data['TextBox2'] = input("请输入密码:")
#
#     return data
#
#
# # 登录教务系统
# def login(url, data):
#     # 通过requests库构造一个浏览器session，这能帮我们自动、持久的管理cookies，
#     s = requests.session()
#     s.post(url, data=data)
#     return s
#
#
# base_url = 'http://jw.gengdan.cn/(ivtfkp45jtlnfgujt4wnsnat)/default2.aspx'
# data = get_post_data(base_url)
# print(data)
# # 模拟登录教务系统
# brow = login(base_url, data)
# test = brow.get(
#     'http://jw.gengdan.cn/(ivtfkp45jtlnfgujt4wnsnat)/xs_main.aspx?xh=180809334')
#
# # 测试看看是否能找到登陆后的信息
# soup = BeautifulSoup(test.text, 'lxml')
# try:
#     name = soup.find('span', attrs={'id': 'xhxm'}).text
# except:
#     name = '登录失败 '
# print(name)
