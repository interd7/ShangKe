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

# goodsInf = [{'name':"联想(Lenovo)小新Pro13高性能轻薄本",'price':'5299'},
#             {'name':"联想(Lenovo)小新Air14性能版轻薄本",'price':'4999'},
#             {'name':"联想(Lenovo)小新15 2020性能版轻薄本",'price':'5199'},
#             {'name':"荣耀笔记本电脑MagicBook",'price':'3499'},
#             {'name':"华为笔记本电脑 MateBook",'price':'4899'},
#             {'name':"宏碁(Acer)暗影骑士·擎",'price':'5899'},
#             {'name':"戴尔DELL灵越5000",'price':'4199'},
#             {'name':"华硕(ASUS) VivoBook15s",'price':'4499'},
#             {'name':"惠普（HP）战66",'price':'4599'},
#             {'name':"Apple MacBook Air 13.3",'price':'5499'}]
# name = sorted(goodsInf,key=lambda x:x["name"],reverse=False)
# for i in name:
#     print(i)
# price = sorted(goodsInf,key=lambda x:int(x['price']),reverse=True)
# for i in price:
#     print(i)
# import random
# for i in range(0,3):
#     for j in range(0,3):
#         print(random.randint(108,111),end="\t")
#     print()

print('===========欢迎使用好友管理系统============')
print('1：添加好友')
print('2：删除好友')
print('3：备注好友')
print('4：展示好友')
print('5：退出')
friends = []
while True:
    sel = int(input('请输入你的选择：'))
    if sel == 1:
        name = input('请输入要添加的好友姓名：')
        friends.append(name)
        print('添加成功')
    elif sel == 2:
        try:
            name = input('请输入要删除的好友姓名：')
            friends.remove(name)
            print('删除成功')
            print(friends)
        except:
            print("好友不存在")
    elif sel == 3:
        try:
            name = input('请输入要备注的好友姓名：')
            elname = input('请输入备注名：')
            friends.remove(name)
            friends.append(elname)
        except:
            print("好友不存在")
    elif sel == 4:
        print(friends)
    else:
        exit()
# import random
# teachers = ['张老师','李老师','黄老师','赵老师','王老师']
# offices  = [[108],[109],[110],[111]]
# # for teacher in teachers:
# #     k = random.randint(0, 3)
# #     print('{}的办公室为{}'.format(teacher,offices[k]))
# for teacher in teachers:
#     i = random.randint(0, 3)
#     offices[i].append(teacher)
# print(offices)
# chinese_num = ('零','壹','贰','叁','肆','伍','陆','柒','捌','玖')
# num = input('请输入数字：')
# for i in num:
#     if i == '.':
#         print('点',end='\t')
#     else:
#         b = eval(i)
#         print(chinese_num[b],end='\t')

