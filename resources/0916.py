# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :0916
# @Date     :2020/9/16 8:30 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import time
'''
0b 二进制
0o 八进制
0x 十六进制
'''
# a = 0b110
# print(a)
# b = 0o111
# print(b)
# c = 0x11
# print(c)

'''
e2 e-2 科学计数法
'''
# a = 3.14e-2
# print(a)

'''
复数
'''
# c1 = 3+2j
# c2 = complex(5,6)
# print(c1)
# print(c2)

'''
bool类型
'''
# b1 = True # 直接赋值
# b2 = False
# b3 = 3<2 # 使用关系表达式
# b2 = bool(0j)
# print(b1)
# print(b2)
# print(b3)

# 类型转换
# a = str(3) # 字符串与数不能相加
# print(a + 6)
# a = int(3.5)
# print(a)

# name = '段益迈'
# age = 18
# province = '山东'
# salary = 999999999.2341235
# print('我的薪水是{:.2f}'.format(salary))
# print('大家好，我是%s，我今年%d岁，来自%s省'%(name,age,province))
# print('大家好，我是{}，今年{}岁'.format(name,age))
# print('大家好，我是%s，我今年%d岁'%(name,age))
# num = 1
# print('{:0>3d}'.format(num))
# num = 0.1
# print('{:0%}'.format(num))
# print(f'我是{name},我今年{age}岁')

# 字符串拼接
# s1 = '人生苦短'
# s2 = '我用Python'
# print(s1 + s2)
# s1 = '大家好，我是段益迈，我今年18岁，来自山东省,18岁真好'
# s2 = s1.replace('18','20',1)
# print(s2)

# senstitive_words = ['北京','上海','黑龙江']
# content = input('请输入：')
# for word in senstitive_words:
#     content = content.replace(word,'*' * len(word))
#
# print(content)
#
# names = '张嘉祺,林庾昊,周磊,庞媛媛,程实,刘佳熠,孙若麟,王天,李明轩,王国礼,陈子涵,邓泽勇,李昊泽'
# name = names.split(sep=',',maxsplit=2)
# for i in name:
#     print('你好：'+i)

# strip() 去除两侧空格
# s1 = '      python      !0000'
# s2 = s1.strip('0')
# print(s2)

# 索引
# str1 = 'Hello Python'
# print(str1[-1])
# print(str1[6])

# 切片
# print(str1[1:10:2])
# print(str1[-7:-1:1])

# for i in range(101):
#     print('{}%'.format(i)+'['+'*'* i +'->'+ '·' * (100-i)+']')
#     time.sleep(0.5)
# print('下载完成！')

# a = 2
# b = 3
# print(a >= 0)
# print(a != 0)
# print(a >= 0 and a <= 100)
# print(not a)
# i = 153
# k1 = i % 10
# print(k1)
# k2 = i//10 % 10
# k3 = i//100 % 10
# print(k2)
# print(k3)
# for i in range(100,1000):
#     k1 = i % 10
#     k2 = i // 10 % 10
#     k3 = i // 100
#     if (k1**3 + k2**3 + k3**3) == i:
#         print(i)

# first_number = input('请输入第一个数')
# second_number = input('请输入第二个数')
# third_number = input('请输入第三个数')
# if first_number>second_number:
#     max_number = first_number
# else: max_number = second_number
# if first_number>third_number:
#     max_number = first_number
# else:max_number = third_number
# if second_number>third_number:
#     max_number = second_number
# else:max_number = third_number
# print(max_number)
# x=10
# y=20
# z=30
# z = x
# x = y
# y = z
# print(x, y, z)
shengao = float(input('请输入您的身高（单位为米）：'))
tizhong = float(input('请输入您的体重（单位为千克）：'))
BMI = tizhong / ( shengao ** 2)
print('您的BMI指数为：{:.2f}'.format(BMI))
if BMI>=30.0:
    print('您肥胖')
elif BMI>=25:
    print('您超重')
elif BMI>=18.5:
    print('您正常')
else:
    print('您偏瘦')

# sheshidu = float(input('请输入摄氏温度：'))
# huashidu = sheshidu*1.8 + 32
# jueduiwendu = sheshidu + 273.15
# lanshidu = sheshidu*1.8+32+459.67
# lieshidu = sheshidu*0.8
# print('{}摄氏温度转为华氏温度为{},绝对温度为{},兰氏度为{:.2f},列氏度为{}'
#       .format(sheshidu,huashidu,jueduiwendu,lanshidu,lieshidu))
# import random
# count = 0
# random_num = random.randint(1, 100)
# while count<5:
#     num = int(input("请猜一个1到100之间的数字："))
#     if num>random_num:
#         print('很遗憾，猜大了')
#     elif num<random_num:
#         print('很遗憾，猜小了')
#     else:
#         print('恭喜你猜对了！')
#         exit()
#     count = count+1
# print('您猜了{}次都没有猜中，再试一次吧！'.format(count))

ipaddr = input('请输入IPv4地址：')
addr = ipaddr.strip().split('.')
if len(addr)==4:
    try:
        for i in range(4):
            addr[i] = int(addr[i])
    except:
        print('IPv4地址不合法，请输入数字，以"."分割。')
        exit()
    if addr[0] > 255 or addr[0] < 0 or addr[1] > 255 or addr[1] < 0 \
            or addr[2] > 255 or addr[2] < 0 or addr[3] > 255 or addr[3] < 0:
        print('IPv4地址不合法，请输入0～255之间的数字。')
    else:
        print('您输入的是合法IPv4地址。')
else:
    print('请输入4段地址。')
