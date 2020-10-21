# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :my_stydy
# @Date     :2020/10/21 9:40 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""


class English:
    def eng_know(self):
        print("具备英语知识")


class Math:
    def math_know(self):
        print("具备数学知识")


class Student(English, Math):
    def show(self):
        print("我是一个学生，我爱学习")
        self.eng_know()
        self.math_know()


z3 = Student()
z3.eng_know()
z3.math_know()
z3.show()
