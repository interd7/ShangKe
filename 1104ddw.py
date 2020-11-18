# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1104ddw
# @Date     :2020/11/4 11:06 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
import re
import json
# page = str(input("请输入页码:"))
# url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}".format(page)
# print(url)
# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68"}

# 发送请求
# response = requests.get(url,headers = headers)
# print(response.text)
from bs4 import BeautifulSoup


def write_item_to_file(item):
    print("开始写入数据===>{}".format(item))
    with open("dangdang.txt","a",encoding="utf-8") as fp:
        fp.write(json.dumps(item,ensure_ascii=False)+"\n")
        fp.close()


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    # 使用lxmlHTML解析器来构造BeautifulSoup对象
    soup = BeautifulSoup(html, 'lxml')
    # 创建空列表Items,用于存放所有有用的数据
    items = []
    # 双重循环，外循环遍历所有包含ul的class为'bang_list clearfix bang_list_mode'的标签
    for li_tag in soup.find_all('ul', {'class': 'bang_list clearfix bang_list_mode'}):
        # 内循环遍历所有li标签
        for div_tag in li_tag.find_all('li'):
            # 每次循环新建空列表item
            item = []
            # 获取num
            num = div_tag.find('div', class_='list_num').text
            # 获取书名
            name = div_tag.find('img').get('alt', '')
            # 获取推荐信息
            tuijian = div_tag.find("span", class_="tuijian").text
            # 获取作者名
            author = div_tag.findAll("div", class_="publisher_info")[0].text
            # 获取日期
            date = div_tag.findAll("div", class_="publisher_info")[1].find('span').text
            # 获取出版社
            publisher = div_tag.findAll("div", class_="publisher_info")[1].find('a').text
            # 获取飙升榜
            biaosheng = div_tag.find("div", class_="biaosheng").find('span').text
            # 获取价格
            price_n = div_tag.find("span", class_="price_n").text
            # 依次追加到列表中
            item.append(num)
            item.append(name)
            item.append(tuijian)
            item.append(author)
            item.append(date)
            item.append(publisher)
            item.append(biaosheng)
            item.append(price_n)
            # 列表嵌套，完成数据临时保存
            items.append(item)
    return items

# 3.通过正则表达式
# ========================================================================
# pattern = re.compile(
    #     '<li>'
    #     '.*?list_num.*?(\d+).</div>'
    #     '.*?<img src="(.*?)"'
    #     '.*?class="name".*?title="(.*?)">'
    #     '.*?class="star">'
    #     '.*?class="tuijian">(.*?)</span>'
    #     '.*?class="publisher_info">.*?target="_blank">(.*?)</a>'
    #     '.*?class="biaosheng">.*?<span>(.*?)</span></div>'
    #     '.*?<p><span\sclass="price_n">¥(.*?)</span>.*?'
    #     '</li>',
    #     re.S)
    # items = re.findall(pattern, html)
    # print(items)
    # return items



def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}".format(page)
    html = request_dangdang(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)

if __name__ == '__main__':
    for i in range(1,26):
        main(i)
