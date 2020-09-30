# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :home0930
# @Date     :2020/9/30 8:26 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# import random
#
# list1 = ['谢谢惠顾','谢谢惠顾','谢谢惠顾','谢谢惠顾','谢谢惠顾','一等奖','二等奖','三等奖']
# random.shuffle(list1)
# i = int(input('请输入刮去位置：（1～8）'))
# loc = i-1
# print(list1[loc])

goodsInf = [{'name':"联想(Lenovo)小新Pro13高性能轻薄本",'price':'5299'},
            {'name':"联想(Lenovo)小新Air14性能版轻薄本",'price':'4999'},
            {'name':"联想(Lenovo)小新15 2020性能版轻薄本",'price':'5199'},
            {'name':"荣耀笔记本电脑MagicBook",'price':'3499'},
            {'name':"华为笔记本电脑 MateBook",'price':'4899'},
            {'name':"宏碁(Acer)暗影骑士·擎",'price':'5899'},
            {'name':"戴尔DELL灵越5000",'price':'4199'},
            {'name':"华硕(ASUS) VivoBook15s",'price':'4499'},
            {'name':"惠普（HP）战66",'price':'4599'},
            {'name':"Apple MacBook Air 13.3",'price':'5499'}]
# name = sorted(goodsInf,key=lambda x:x["name"])
# for i in name:
#     print(i)
price = sorted(goodsInf,key=lambda x:int(x['price']))
for i in price:
    print(i)
