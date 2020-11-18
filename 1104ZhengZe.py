# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1104ZhengZe
# @Date     :2020/11/4 8:41 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import re

# \d 匹配任意的数字

# string = "123gengdan456"
# result = re.match("\d",string)
# print(result.group())

# \D 匹配非数字

# string = "s23gengdan456"
# result = re.match("\D",string)
# print(result.group())

# \w 匹配字母数字下划线 a-z A-z 0-9 _

# string = "gengdan"
# result = re.match("\w",string)
# print(result.group())

# \W 与\w相反

# string = "·gengdan"
# result = re.match("\W",string)
# print(result.group())

# \s 匹配空白字符 包括(\n \t \r)

# string1 = r"Geng\ndan"
# string = " Geng\ndan"
# result = re.match("\s",string)
# print(string1)
# print(result.group())

# \S匹配非空白字符

# string = "Gengdan"
# result = re.match("\S",string)
# print(result.group())

# []组合的方式，只要满足中括号中某一项，就算匹配成功
# [0-9] \d
# [^0-9] \D
# [a-zA-Z0-9_] \w
# [^a-zA-Z0-9_] \W
# string = "gengdan"
# result = re.match("[a-z1-3]", string)
# print(result.group())

# 多个字符
# * 匹配0个或多个字符
# string = "geng+dan"
# result = re.match("\w*", string)
# print(result.group())

# + 匹配1个或多个字符
# string = "0a!!g33!asdasd"
# result = re.match("\d+", string)
# print(result.group())

# ? 匹配0-1个字符
# string = "0a!!g33!asdasd"
# result = re.match("\w?", string)
# print(result.group())

# {m} 匹配m个字符
# string = "abca!!g33!asdasd"
# result = re.match("\w{4}", string)
# print(result.group())

# {m,n} 匹配m-n个字符
# string = "ca!!g33!asdasd"
# result = re.match("\w{0,4}", string)
# print(result.group())

# ^...... 以......开头
# string = "gengdan2020 2020"
# result = re.match("^gen", string)
# print(result.group())

# $...... 以......结尾 ｜  match 从左往右 ｜  search查找
# string = "gengdan2020"
# result = re.search("2020$", string)
# print(result.group())

# | 匹配多个字符串或者表达式(相当于或)
# string = "http://www.baidu.com"
# result = re.match("https|http|ftp",string)
# print(result.group())

# 贪婪和非贪婪
# # 提取html标签
# text = "<h1>这是h1标题</h1>"
# # 贪婪
# result = re.match("<.+>",text)
# # 非贪婪
# result1 = re.match("<.+?>",text)
# print(result1.group())

# 匹配手机号
# my_phone_number = "15069131111"
# regex = "1[345789][0-9]{9}"
# result = re.match(regex,my_phone_number)
# print(result.group())

# 匹配邮箱
# email = "inter@163.com"
# regex = ".+@[a-z0-9]+\.[a-z]+"
# result = re.match(regex, email)
# print(result.group())

# () 分组  \ 后为转义字符

# text = "The price of apple is $3,the price of orange is $4"
# regex = ".+(\$\d).+(\$\d)"
# result = re.search(regex, text)
# print(result.group(1))
# print(result.group(2))

# 贪婪和非贪婪


# 提取html标签
text ="""
<div>北京工业大学耿丹学院2020年招生宣传册(内附专业介绍)</div>
<div>北京工业大学耿丹学院2020年报考指南</div>
<div>积极开展体育健身锻炼 实现立德树人根本任务</div>
<div>国际交流办公室举办加拿大卡普顿大学硕士课程宣讲会</div>
<div>中华文化初体验之时光穿梭</div>
<div>工学院工业设计专业受邀参加第14届CLE中国授权展</div>
<div>环境设计专业举办风景园林植物课程展</div>
<div>Oh My GAD——视觉探索线上展览</div>"
"""

# res_tr = r'<div>(.*?)</div>'
#
# m_tr =  re.findall(res_tr,text)
#
# for line in m_tr:
#     print(line)

# findall 函数
# string = "hello world Hello python hello java"
# result = re.findall("hello (\w+)",string,re.I)
# print(result)
# print(result[2])

# 替换
# new_html = re.sub("<.+?>","",text)
# print(new_html)

