# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:使用标签和按钮的简单窗体
# @Date     :2020/11/25 9:14 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter

root = tkinter.Tk()
root.title("Hello GUI")
root.geometry("300x200") # 设置窗口大小(长 x 宽)

label = tkinter.Label(root,text = 'Hello,GUI') # 生成标签
label.pack() # 将标签添加到主窗口

button1 = tkinter.Button(root, text='Button1')
button2 = tkinter.Button(root, text='Button2')

button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.RIGHT)

root.mainloop()
