# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :person
# @Date     :2020/10/21 8:41 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""

class Person:
    # 属性、字段
    name = '张三'
    __age = 18
    __weight = 50

    @classmethod
    def f(cls):
        cls.name = "小段"
        print(cls.name)
        pass

    # 方法
    def show(self):
        # self.name = "李四"
        self.__age = 19
        print("姓名：", self.name)
        print("年龄：", self.__age)
        print("体重：", self.__weight)

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def __init__(self, id):
        self.__id = id
        print("我出生了！")

    def get_id(self):
        return self.__id

    def __del__(self):
        print("我牺牲了！")
# print(Person.name)
# # 构造一个对象
# z3 = Person()
# print(z3.name)
# z3.show()
l4 = Person(1808)
# l4.name = "李小五"
# Person.name = "王小五"
# Person.__age = 20
# l4.show()
# l4.set_weight(51)
# l4.show()
# print(l4.get_weight())
w5 = Person(188)
print(l4.get_id())
Person.f()
