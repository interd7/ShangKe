# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :test
# @Date     :2020/10/21 8:50 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from my_class_demo.person import Person

l4 = Person(188)
l4.name = "李小五"
Person.name = "王小五"
l4.show()
