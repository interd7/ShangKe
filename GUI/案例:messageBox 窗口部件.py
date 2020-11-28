# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:messageBox 窗口部件
# @Date     :2020/11/25 10:33 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter as tk  # 使用 Tkinter 前需要先导入
import tkinter.messagebox  # 要使用 messagebox 先要导入模块

# 第 1 步，实例化 object，建立窗口 window
window = tk.Tk()
# 第 2 步，给窗口的可视化起名字
window.title('messagebox 用法')
# 第 3 步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小 x


# 第 5 步，定义触发函数功能
def hit_me():
    tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗


# 第 4 步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), fg='white', command=hit_me).pack()
# 第 6 步，主窗口循环显示
window.mainloop()
