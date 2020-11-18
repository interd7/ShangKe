# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :bs4_demo
# @Date     :2020/11/11 10:40 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from bs4 import BeautifulSoup
html = '''
<!DOCTYPE html>  
<html lang="en">  
  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>北京工业大学耿丹学院</title>  
</head>  
  
<body>  
    <p class="title"><b>耿丹学院</b></p >  
  
    <p class="college">二级学院  
        <a href="http://example.com/1" class="sister" id="link1">工学院、商学院</a >,  
        <a href="http://example.com/2" class="sister" id="link2">人文学院</a >、艺术学院  
    </p >  
  
    <p class="story">  
        北京工业大学耿丹学院创建于 2005 年，是经国家教育部批准成立的一所全日制民办普通本科院校。  
    </p >  
</body>  
  
</html>
'''
soup = BeautifulSoup(html,"lxml")
    # 提取网页中的title
# print(soup.title.string)
# print(soup.p)
# print(soup.a)
#   提取标签里的内容  .string
# print(soup.title.string)
# print(soup.b.string)
# print(soup.find_all("a")[1].string)
# print(soup.get_text())

# find

# print(soup.find("p", class_="story"))
# print(soup.find("p", class_="college"))

# css select

# print(soup.select(".college"))
# print(soup.select("#link2"))
print(soup.select("title"))
