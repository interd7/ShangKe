# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :0930
# @Date     :2020/9/30 8:42 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
list1 = [1, "3", 5, 7.2, 9]
list2 = list('Hello Python')
# list2 = list(list1)
t1 = (1,3,4,5)
t2 = {1, 2, 3, 4, 5}
list3 = list('1222333')# 一个参数，或一个可迭代类型的数据（字符串，列表，元祖，字典，集合）
# print(list2)
# 字符串
s1 = "hello world!"
for s in s1:
    print(s)
# 遍历列表
for i in list3:
    print(i,end='\t')
