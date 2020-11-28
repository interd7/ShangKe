# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:菜单
# @Date     :2020/11/25 11:07 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from tkinter import *


class MenuDemo:
    def hello(self):
        print("hello!")

    def __init__(self):
        self.window = Tk()
        self.window.title("Menu demo")

        menubar = Menu(self.window, bg="red")
        self.window.config(menu=menubar)

        # 创建下拉菜单，并添加到菜单条
        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="操作", menu=operationMenu)
        operationMenu.add_command(label="加", command=add)
        operationMenu.add_command(label="减", command=subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="乘", command=multiply)
        operationMenu.add_command(label="除", command=divide)
        exitMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="退出", menu=exitMenu)
        exitMenu.add_command(label="退出", command=self.window.quit)

        # 窗口中放入一个文本框
        self.txtcontent = Text()
        self.txtcontent.insert('end', "请选择您要进行的操作！")
        self.txtcontent.pack()
        mainloop()


def add(self):
    self.txtcontent.delete('1.0', 'end')
    self.txtcontent.insert("insert", "相加")
    print("相加")


def subtract(self):
    self.txtcontent.delete('1.0', 'end')
    self.txtcontent.insert("insert", "相减")
    print("相减")


def multiply(self):
    self.txtcontent.delete('1.0', 'end')
    self.txtcontent.insert("insert", "相乘")
    print("相乘")


def divide(self):
    self.txtcontent.delete('1.0', 'end')
    self.txtcontent.insert("insert", "相除")
    print("相除")


MenuDemo()
