# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1007
# @Date     :2020/10/7 8:30 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
'''
dict1 = {}
dict2 = {'姓名':'张三','年龄':18}
print(dict2['姓名'])
dict3 = dict(姓名 = '段益迈',年龄 = 20)
dict3 = dict({'姓名':'张三','年龄':18})
print(dict3)
color_dict = {'red' : '红色', 'green' : '绿色', 'blue' : '蓝色'}
print(color_dict['blue'])
if 'purple' in color_dict:
    print(color_dict['purple'])
else:
    print('对不起，键不存在')

if 'purple' not in color_dict:
    print('对不起，键不存在')
else:
    print(color_dict['purple'])
    
'''

# dict_day = {'M':'Monday','T':'Tuesday','W':'Wednesday','TH':'Thursday','F':'Friday','S':'Saturday','Su':'Sunday'}
# day = input('请输入键:\n')
# try:
#     print(dict_day[day])
# except:
#     print('对不起，键不存在')
# set1 = {1, 2, 3, 4}
# set1.add('')
# set1.update('')
# set1.remove('')
# set1.discard('')
# set1.pop()
# set1.clear()
'''
set_a = { 1, 3, 5, 7, 9}
set_b = { 1, 2, 3, 4, 5, 6, 7}
# 并
print(set_a | set_b)
# 交
print(set_a & set_b)
# 差补 (在a 不在b)
print(set_a - set_b)
# 对称差分 (相对补集的并集)
print(set_a ^ set_b)
'''
# def f1():
#     print('****************')
#
# def f2(n):
#     print('*' * n)
# # f1()
# f2(10)
# lan_info = {'01': 'Python', '02': 'Java', '03': 'PHP'}
# lan_info.update({'03': 'C++'})
# print(lan_info)
# set_01 = {'a', 'c', 'b', 'a'}
# set_01.add('d')
# print(len(set_01))
test_two = {'a': 'A'}
print(test_two)
