# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :apple
# @Date     :2020/10/21 9:20 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""


class Apple:
    count = 10
    def show(self):
        print("我是Apple的show方法")
    def __init__(self,id):
        print("我是Apple的构造方法")
    # def f1(self):
    #     self.count = 88
    #
    # @classmethod
    # def f2(cls):
    #     cls.count = 99
    #
    # @staticmethod
    # def f3():
    #     Apple.count = 111
    #     print(Apple.count)
    #     # Apple.f2()


class Hfsapple(Apple):
    weight = 0.5
    def __init__(self,id):
        super(Hfsapple, self).__init__(id)
        print("我是hfs的构造方法")
    def show(self):
        super().show()
        print(self.weight,Hfsapple.count)

# a = Apple()
# a.f1()
# print(Apple.count)
# print(a.count)
# Apple.f2()
# print(Apple.count)

# Apple.f3()
a1 = Hfsapple(1)
a1.show()
