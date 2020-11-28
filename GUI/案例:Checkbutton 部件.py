# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:Checkbutton 部件
# @Date     :2020/11/25 9:50 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter as tk  # 使用 Tkinter 前需要先导入

# 第 1 步，实例化 object，建立窗口 window
window = tk.Tk()
# 第 2 步，给窗口的可视化起名字
window.title('Checkbutton 用法')
# 第 3 步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小 x
# 第 4 步，在图形界面上创建一个标签 label 用以显示并放置
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


# 第 6 步，定义触发函数功能
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):  # 如果选中第一个选项，未选中第二个选项
        l.config(text='我只爱 Python ')
    elif (var1.get() == 0) & (var2.get() == 1):  # 如果选中第二个选项，未选中第一个选项
        l.config(text='我只爱 Java')
    elif (var1.get() == 0) & (var2.get() == 0):  # 如果两个选项都未选中
        l.config(text='这两个编程语言我都不喜欢')
    else:
        l.config(text='这两个编程语言我都喜欢')  # 如果两个选项都选中


# 第 5 步，定义两个 Checkbutton 选项并放置
var1 = tk.IntVar()  # 定义 var1 和 var2 整型变量用来存放选择行为返回值
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)  # 传值原理类似于 radiobutton 部件
c1.pack()
c2 = tk.Checkbutton(window, text='Java', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
# 第 7 步，主窗口循环显示
window.mainloop()
