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
import os
print('===========欢迎通讯录管理系统============')
print('1：增加姓名和手机')
print('2：删除姓名')
print('3：修改手机')
print('4：查询所有用户')
print('5：根据姓名查找手机号')
print('6：退出')
dict = {}
def create_add():
    name = input('请输入姓名：')
    phone = input('请输入手机号：')
    dict[name] = phone
    address = name + ':' + phone+'\n'
    with open('address.txt', 'a', encoding='utf-8')as fp:
        fp.write(address)
    print('添加完成')
def del_add():
    try:
        name = input('请输入要删除的联系人：')
        del dict[name]
        print('删除成功')
    except:
        print("联系人不存在")
def el_add():
    name = input('请输入要修改的联系人：')
    if name in dict:
        phone = input('请输入要修改的电话号码：')
        dict[name] = phone
        print('手机号修改成功！')
    else:
        print("联系人不存在！")
def show_add():
    for i in dict:
        print('{}\t{}\n'.format(i, dict[i]))
def search_add():
    name = input('请输入您要查询的联系人：')
    print(dict[name])
while True:
    sel = int(input('请输入你的选择：'))
    if sel == 1:
        create_add()
    elif sel == 2:
        del_add()
    elif sel == 3:
        el_add()
    elif sel == 4:
        show_add()
    elif sel == 5:
        search_add()
    else:
        print()
        print('已退出！')
        exit()
    print('请按enter继续！')
    os.system("read -rsp $'Press enter to continue...\n' ")

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
# while 1:
#     try:
#         a = int(input("输入被除数："))
#         b = int(input("输入除数："))
#         c = a / b
#         print("您输入的两个数相除的结果是：", c)
#     except (ValueError, ArithmeticError):
#         print("程序发生了数字格式异常、算术异常之一")
#     except:
#         print("未知异常")
#     print("程序继续运行\n")
