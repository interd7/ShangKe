# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:创建一个空白窗体
# @Date     :2020/11/25 9:10 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter
# 使用tkinter.Tk()生成主窗口
win = tkinter.Tk()
# 设置窗体标题
win.title("案例创建空白窗体")
# 500x300为窗口大小，+200+200为窗体位置
win.geometry("500x300+200+200")
# 进入消息循环
win.mainloop()
