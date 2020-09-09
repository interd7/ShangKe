# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :0906
# @Date     :2020/9/6 10:53 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import random

'''
print('\033[0;31m★★★★★\033[0m')
print('★★★★★')
print('\033[0;32m★★★★★\033[0m')
print('\033[0;35m★★★★★\033[0m')
print('\033[0;31;43m★★★★★\033[0m')

print('Hello，world')
print('我的学号:'+'180809329'+'我的姓名：'+'段益迈')
print()
print(3)
print(3+3)
print('你好：'+'耿丹')
print('name=段益迈')
print('我有几个苹果：',2,3,4,5,6)
print(192,168,3,40,sep=':')
print('age=',18, end=' ')
print('今天是星期'+str(5))
print('%.2f' % 3.1415926)
print('{:.2f}'.format(3.1415926))
print(round(3.1415916,2))
with open('test.txt','w',encoding='utf-8')as f:
    print('我在练习向文件中写入数据:\n','Hello Python!','Hello Java!', '\nSee you!',sep='********',end='',file=f)
with open('test.txt','r',encoding='utf-8')as f:
    data = f.read()
    print(data)


name = input('请输入姓名：')
age = input('请输入年龄：')
os = eval(input('您的操作系统成绩：'))
py = int(input('您的Python成绩：'))
salary = eval(input('您的暑期实习工资：'))
print('宁的姓名为：',name)
print('宁的年龄为：',age)
print('您的操作系统成绩：',os)
print('您的平均成绩：',(os + py)/2)
print('您的暑期实习工资：',salary)


print('用法1：将整形或者浮点数类型转为str字符串类型')
print(type(str(3.14)))
print(str(3.14))
print('***' * 20)

print('用法2：将字典转为str字符串类型')
dict1 = {'小李':19,'小段':20,'小强':20}
print(type(str(dict1)))
print(str(dict1))
print('***' * 20)

print('用法3：将列表转为str字符串类型')
list1 = [1, 2, 3, 4, 5, 6]
print(type(str(list1)))
print(type(list1))
print(list1)
print(str(list1))

print("{} {}".format("hello", "world"))
print("{0} {1}".format("hello", "world"))
print("{1} {0} {1}".format("hello", "world"))
print("网站名：{name}, 地址 {url}".format(name="北京工业大学耿丹学院1", url="www.gengdan.cn"))
site = {"name": "北京工业大学耿丹学院2", "url": "www.gengdan.cn"}
print("网站名:{name}, 地址 {url}".format(**site))
my_list = ["北京工业大学耿丹学院3", "www.gengdan.cn"]
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))

print("{:.2f}".format(3.1415926))
print("{:+.2f}".format(3.1415926))
print("{:.0f}".format(3.1415926))
print("{:0>10d}".format(12345))
print("{:x<10d}".format(12345))
print("{:,}".format(12345))
print("{:.2%}".format(0.25678))
print("{:.2e}".format(123456))
print("{:>10d}".format(123456))
print("{:<10d}".format(123456))
print("{:^10d}".format(123456))

print("{:b}".format(11))
print("{:d}".format(11))
print("{:o}".format(11))
print("{:x}".format(31))
print("{} 对应的位置是 {{0}}".format("gengdan"))


print('产生一个[0,1)之间的随机实数：',random.random())
print('产生一个[0,1)之间的随机实数：',random.random())
print('产生1.1到5.4之间的随机浮点数，区间可以不是整数：',random.uniform(1.1,5.4))
print('从gengdan序列中随机选取一个元素：',random.choice('gengdan'))
print('随机选取字符串：',random.choice(['剪刀','石头','布']))
print('生成从1到100的间隔为2的随机整数：',random.randrange(1, 100, 2))
print('将序列a中的元素顺序打乱：')
a = [1, 3, 5, 7, 9]
print('原始列表：', a)
random.shuffle(a)
print('打乱后的列表：', a)

# print('段益迈180809329')
phone_num = input("请输入你要充值的手机号：")
jine = input('请输入要充值的金额：')
print('手机号码'+phone_num+'成功充值'+jine)

km = input("请输入海洋公里数：")
haimiles = float(km) / 1.852
print('海里数为：', round(haimiles, 2))
'''

