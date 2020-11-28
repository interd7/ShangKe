# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:Scale 窗口部件
# @Date     :2020/11/25 9:55 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter as tk  # 使用 Tkinter 前需要先导入

# 第 1 步，实例化 object，建立窗口 window
window = tk.Tk()
# 第 2 步，给窗口的可视化起名字
window.title('Scale 用法')
# 第 3 步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小 x
# 第 4 步，在图形界面上创建一个标签 label 用以显示并放置
l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()


# 第 6 步，定义一个触发函数功能
def print_selection(v):
    l.config(text='您的评价分值为：' + v)


# 第 5 步，创建一个尺度滑条，长度 200 字符，从 0 开始 10 结束，以 2 为刻度，精度为 0.01，触发调用 print_selection 函数
s = tk.Scale(window, label='给我评价：', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2,
             resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
