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
    age = 18

    # 方法
    def show(self):
        self.name = "李四"
        print("姓名：",self.name)
        print("年龄：",self.age)

print(Person.name)
# 构造一个对象
z3 = Person()
print(z3.name)
z3.show()
