# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1111beautifulsoup
# @Date     :2020/11/11 9:41 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""

from bs4 import BeautifulSoup
import requests

html = """ 
<html>
<head>
    <title>The Dormouse's story</title>
</head>

<body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p >
    <p class="story">Once upon a time there were three little sisters; and their names were < a href=" " class="sister"
            id="link1">
            <!-- Elsie -->
        </ a>, < a href="http://example.com/lacie" class="sister" id="link2">Lacie</ a> and < a
            href="http://example.com/tillie" class="sister" id="link3">Tillie</ a>; and they lived at the bottom of a
        well.</p >
    <p class="story">...</p >
</body>
</html>
"""
html1 = """
<div>
    <a>
        <p></p>
        <p></p>
        <p></p>
    </a>
</div>
"""
html3=''' <div class="panel"> <div class="panel-heading"> <h4>Hello</h4> </div> <div class="panel-body"> <ul class="list" id="list-1"> <li class="element">Foo</li> <li class="element">Bar</li> <li class="element">Jay</li> </ul> <ul class="list list-small" id="list-2"> <li class="element">Foo</li> <li class="element">Bar</li> </ul> </div> </div> '''
soup = BeautifulSoup(html3,"lxml")
# text = soup.find_all("ul")
# body = soup.find("body")
body = soup.p
print(body)
# print(list(enumerate(soup.div.children)))
# print(list(enumerate(soup.div.descendants)))
# print(list(enumerate(soup.p.parents)))
# print(list(enumerate(soup.p.next_siblings)))
# print(soup.p)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)
# print(soup.title.parent.parent.name)
# print(soup.p.string)
