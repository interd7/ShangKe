# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :animal
# @Date     :2020/10/21 9:45 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
class Animal:
    def move(self):
        print("动物在移动")
class Rabbit(Animal):
    def move(self):
        print("兔子跳")
class Snail(Animal):
    def move(self):
        print("慢慢爬")

def f(obj):
    obj.move()

r1 = Rabbit()
f(r1)
s1 = Snail()
f(s1)
