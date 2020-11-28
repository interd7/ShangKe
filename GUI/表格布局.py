# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :表格布局
# @Date     :2020/11/25 9:07 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter

win = tkinter.Tk()
win.title("表格布局")
win.geometry("300x300+100+200")

label1 = tkinter.Label(win, text="我是标签1", bg="pink")
label2 = tkinter.Label(win, text="我是标签2", bg="yellow")
label3 = tkinter.Label(win, text="我是标签3", bg="red")
label4 = tkinter.Label(win, text="我是标签4", bg="green")
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

win.mainloop()
