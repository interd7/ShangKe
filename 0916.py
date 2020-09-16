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

for i in range(101):
    print('{}%'.format(i)+'['+'*'* i +'->'+ '·' * (100-i)+']')
    time.sleep(1)
print('下载完成！')

