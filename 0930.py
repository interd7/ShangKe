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
# s1 = "hello world!"
# for s in s1:
#     print(s)
# # 遍历列表
# for i in list3:
#     print(i,end='\t')
# list4 = ["Java","C#","C","C++",["Python","VB"]]
# print(list4[-1][1])
# print(list4[:])
# print(list4[:3])
# print(list4[3:])
# print(list4[::-1])

# def add(x,y):
#     return x + y
# print(add(3, 4))

# goods_list = [[1, 399],[2, 4369],[3, 5329],[4, 288]]

# li_one = ['p', 'c', 'q', 'h']
# li_two = ['o']
# li_one.extend(li_two)
# li_one.insert(2, 'n')
# print(li_one)

# list1 = [1, 2, 3, 4]
# print(sum(list1), end="\t")
# print(min(list1), end="\t")
# print(max(list1), end="\t")

# li_one = [2, 1, 5, 6]
# print(sorted(li_one[:2]))

t1 = ()
t2 = (1, 2, 3, '4', 3.25)
t3 = (1,)
t4 = tuple('hello python!')
list1 = [['julia'], 'kate', 'kitty']
t5 = tuple(list1)
print(t5)
t5[0].append(88)
print(t5)

