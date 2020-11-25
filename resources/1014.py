# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1014
# @Date     :2020/10/14 8:47 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""


#
#
# def f1():
#     print("*")
#
#
# def f2(n):
#     print("*" * n)
#     pass
#
#
# def f3(a, b, c):
#     return a + b + c
#
#
# f1()
# f2(100)
# i = 5
# j = 2
# # c = f3(5, 2, 0)
# c = f3(a=5, c=3, b=4)
# print(c)
#
#
# def f4(name, age, add):
#     print("--------------个人信息--------------")
#     print("姓名", name)
#     print("年龄", age)
#     print("地址", add)
#     pass
#
#
# f4("dym", 18, "北京")
# f4(name="dym", age=18, add="北京")
# f4(name="dym", add="北京", age=18)
# f4(age=18, name="dym", add="北京")
# f4(age=18, add="北京", name="dym")
# f4(add="北京", name="dym", age=18)
# f4(add="北京", age=18, name="dym")
#

# def f5(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# f5(1, 2, 3, 4, 5)
# x = 99
# def f8():
#     # global 全局变量
#     # global x
#     x = 88
#     print("函数内部", x)
#
# f8()
# print("函数外部", x)
#
# div = lambda x, y: x / y
# print(div(9, 3))

# 非递归，求阶乘

# n! = n * (n-1) * ......* 2 * 1

# def jic(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     print(result)
# jic(5)

def jic(n):
    if n == 1:
        return 1
    else:
        return n * jic(n - 1)


print(jic(5))
