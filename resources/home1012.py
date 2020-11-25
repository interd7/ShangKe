# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :home1012
# @Date     :2020/10/12 4:02 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""

# def compute(x, y):
#     if sign == '+':
#         return x + y
#     elif sign == '-':
#         return x - y
#     elif sign == '*':
#         return x * y
#     elif sign == '/':
#         return x / y
#     else:
#         print('运算符错误！')
#
# x = float(input("请输入第一个数："))
# y = float(input("请输入第二个数："))
# sign = input("请选择要执行的运算符：+、-、*、/\n")
# print('计算结果是{}'.format(compute(x, y)))

# #
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# # 获取用户输入
# nterms = int(input("您要输出几项? "))
# count = 0
# # 检查输入的数字是否正确
# a = 0
# b = 1
# sums = 0
# for _ in range(nterms + 1):
#     sums += a
#     a, b = b, a + b
# if nterms <= 0:
#     print("输入正数")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms):
#         print(recur_fibo(i + 1), end=' ')
#         count += 1
#         if count % 10 == 0:
#             print()
#     print('============================================================s')
#     print('sum = {}'.format(sums))

import os
import time
import pygame

# file = r'/Users/inter.d/Downloads/music/李荣浩 - 不将就.wav'
music_list = [r'/Users/inter.d/Downloads/music/李荣浩 - 不将就.wav',
              r'/Users/inter.d/Downloads/music/李荣浩 - 老街.wav',
              r'/Users/inter.d/Downloads/music/王力宏 - 心跳.wav']
print("-------------简单的音乐播放器-------------")
print("1.播放")
print("2.暂停")
print("3.恢复")
print("4.停止")
print("5.上一首")
print("6.下一首")
print("0.退出")

i: int = 0


def play_music():
    # 初始化音频部分
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load(music_list[i])
    pygame.mixer.music.play()
    print("开始播放")
    pass


def pause_music():
    pygame.mixer.music.pause()
    pass


def unpause_music():
    pygame.mixer.music.unpause()
    pass


def stop_music():
    pygame.mixer.music.stop()
    pass


def previous():
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load(music_list[i])
    pygame.mixer.music.play()
    print("上一首")


def next():
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load(music_list[i])
    pygame.mixer.music.play()
    print("下一首")


while True:
    check = input("请输入你的选择：")
    if check == '1':
        play_music()
    elif check == '2':
        pause_music()
    elif check == '3':
        unpause_music()
    elif check == '4':
        stop_music()
    elif check == '5':
        i = int(i - 1)
        if i < 0:
            i = 2
        previous()
    elif check == '6':
        i = int(i + 1)
        if i > 2:
            i = 0
        next()
    elif check == '0':
        print("运行结束！")
        exit()
