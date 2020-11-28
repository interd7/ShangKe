# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :GUI_1
# @Date     :2020/11/25 8:55 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter

win = tkinter.Tk()
win.title("绝对布局")  # 窗口标题
win.geometry("600x500+200+20")  # 窗口位置 500后面是字母x
'''
绝对布局
'''
label1 = tkinter.Label(win, text="我是标签1", bg="pink")
label2 = tkinter.Label(win, text="我是标签2", bg="yellow")
label3 = tkinter.Label(win, text="我是标签3", bg="red")
# 默认没有布局，字有多长，背景也有多长，和其他label错落显示

# label1.pack()
# label2.pack()
# label3.pack()

# 固定坐标
label1.place(x=10, y=10)
label2.place(x=100, y=150)
label3.place(x=200, y=290)
win.mainloop()
