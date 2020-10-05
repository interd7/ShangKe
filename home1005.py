# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :home1005
# @Date     :2020/10/5 8:37 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""

# print('===========欢迎通讯录管理系统============')
# print('1：增加姓名和手机')
# print('2：删除姓名')
# print('3：修改手机')
# print('4：查询所有用户')
# print('5：根据姓名查找手机号')
# print('6：退出')
# dict = {}
# while True:
#     sel = int(input('请输入你的选择：'))
#     if sel == 1:
#         name = input('请输入姓名：')
#         phone = input('请输入手机号：')
#         dict[name] = phone
#         print('添加完成')
#     elif sel == 2:
#         try:
#             name = input('请输入要删除的联系人：')
#             del dict[name]
#             print('删除成功')
#         except:
#             print("联系人不存在")
#     elif sel == 3:
#         try:
#             name = input('请输入要修改的联系人：')
#             phone = input('请输入要修改的电话号码：')
#             dict[name] = phone
#             print('手机号修改成功！')
#         except:
#             print("联系人不存在！")
#     elif sel == 4:
#         print(dict)
#     elif sel == 5:
#         name = input('请输入您要查询的联系人：')
#         print(dict[name])
#     else:
#         print()
#         print('已退出！')
#         exit()

# urls=['https://www.baidu.com/',
# 'https://www.ketangpai.com/',
# 'http://www.gengdan.cn/',
# 'http://www.gengdan.cn/',
# 'http://kq.gengdan.cn/',
# 'https://www.yuque.com/',
# 'https://www.yuque.com/']
#
# url = set(urls)
# print(url)
# import random
# student = set()
# while len(student)<20:
#    a = random.randint(1,2)
#    b = random.randint(1,50)
#    c = str(b)
#    if b<10:
#        c='0'+c
#    x = '202009'+str(a)+c
#    student.add(x)
# print('本次毕业设计抽查的学号为：')
# print('==============================')
# j = 0
# for i in student:
#     print(i,end='\t')
#     j += 1
#     if j == 5:
#         print()
#         j = 0
#
