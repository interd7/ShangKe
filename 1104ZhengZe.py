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
string = "geng+dan"
result = re.match("\w*", string)
print(result.group())
