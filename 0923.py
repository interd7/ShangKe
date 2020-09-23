# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :0923
# @Date     :2020/9/23 8:36 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""

# number = int(input("请输入4位数:"))
# k1 = number % 10
# k2 = number // 10 % 10
# k3 = number // 100 % 10
# k4 = number // 1000
#
# if k1 == k4 and k2 == k3:
#     print("{}是回文数".format(number))
# else:
#     print("{}不是回文数".format(number))
# lirun = float(input("请输入利润：(万元)"))
#
# if lirun <= 10:
#     bili = 0.1
#     ticheng = lirun * bili
#     print("奖金提成为{}万元".format(ticheng))
# elif lirun <= 20:
#     bili = 0.075
#     ticheng = lirun * bili
#     print("奖金提成为{}万元".format(ticheng))
# elif lirun <= 40:
#     bili = 0.03
#     ticheng = lirun * bili
#     print("奖金提成为{}万元".format(ticheng))
# elif lirun <= 60:
#     bili = 0.015
#     ticheng = lirun * bili
#     print("奖金提成为{}万元".format(ticheng))
# else:
#     bili = 0.01
#     ticheng = lirun * bili
#     print("奖金提成为{}万元".format(ticheng))
# for i in range(1, 101):
#     if i % 7==0 or i % 10 == 7 or i // 10 == 7:
#         print("**", end="\t")
#     else:
#         print(i, end='\t')
#     if i % 10 == 0:
#         print(" ")
# 判断登录

# i = 1
# while i <= 3:
#     i += 1
#     Name = input('输入用户名： ')
#     Password = input('输入用户密码： ')
#     if Name == 'dym0822' and Password == '123456':
#         print('登陆成功！')
#         exit()
#     else:
#         print('登陆失败')
#         print('还剩下{}次机会\n'.format(4-i))
# else:
#     print('错误次数超过3次！已锁定！')

# 99乘法表
# for j in range(1, 10):
#     for i in range(1, j+1):
#         result = i * j
#         if i <j:
#             print(i,'*',j, '=', result, ' ', end = ' ')
#
#         else:
#             print(i,'*',j,'=',result,' ')

# 随机生成六位验证码
# import random
# randomStr = ""
#
# for i in range(6):
#     temp = random.randrange(0, 3)
#     if temp == 0:
#         ch = chr(random.randrange(ord('A'), ord('Z') + 1))
#         randomStr += ch
#     elif temp == 1:
#         ch = chr(random.randrange(ord('a'), ord('z') + 1))
#         randomStr += ch
#     else:
#         ch = str((random.randrange(0, 10)))
#         randomStr += ch
#
# print(randomStr)

# 掷骰子
import cv2
import time
import random
inx = input('按回车开始掷色子!!').strip()
for i in range(10):
    cv2.waitKey(1)
    # 将程序停顿0.5秒  
    time.sleep(0.5)
    # 产生[1,6]之间的随机数  
    j = random.randint(1, 6)
    imgj = str(j) + 'a.png'
    # 读取图片  
    img = cv2.imread(imgj)
    # 显示图片  
    cv2.imshow("img", img)

print('您投中了{}点！'.format(j))
# 关闭窗口  
# cv2.destroyAllWindow() 
