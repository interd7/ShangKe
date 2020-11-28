# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :GUI_2
# @Date     :2020/11/25 9:02 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter

win = tkinter.Tk()
win.title("相对布局")  # 窗口标题
win.geometry("600x500+200+20")  # 窗口位置

'''
相对布局，窗体改变对空间有影响
'''
label1 = tkinter.Label(win, text="我是标签1", bg="pink")
label2 = tkinter.Label(win, text="我是标签2", bg="yellow")
label3 = tkinter.Label(win, text="我是标签3", bg="red")
# 相对布局
label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.X, side=tkinter.TOP)
label3.pack()

win.mainloop()
