# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:Entry窗口部件
# @Date     :2020/11/25 9:33 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter as tk

win = tk.Tk()

win.title('Entry用法')

win.geometry('500x300')

# 在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(win, show='*',font=('Arial', 14))# 密文
e2 = tk.Entry(win, show=None,font=('Arial', 14))# 明文
e1.pack()
e2.pack()

win.mainloop()
