# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:按钮的单击事件
# @Date     :2020/11/25 9:20 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter as tk

# 1.实例化object,建立窗口window
win = tk.Tk()

# 2.给窗口的可视化起名字
win.title('按钮的使用方法')

# 3.设定窗口的(长 x 宽)
win.geometry('500x300')

# 4.在图形界面上设定标签
var = tk.StringVar()  # 将 label 标签的内容设置为字符类型，用 var 来接收 click_me函数的传出内容用以显示在标签上

l = tk.Label(win, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
l2 = tk.Label(win, bg = 'red',text='你好')
# 说明： bg 为背景，fg 为字体颜色，font 为字体，width 为长，height 为高，这里的长和高是字符的长和高，比如 height=2,就是标签有 2 个字符这么高
l.pack()
l2.pack()
#  定义一个函数功能（供点击 Button 按键时调用，调用命令参数 command=函数名）
on_hit = False
def click_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('你单击了我！')
        l2.config(text='点击')
    else:
        on_hit = False
        var.set('')

# 5.在窗口界面设置放置Button按键
b = tk.Button(win, text='确定',font=('Arial', 12),width=10,height=1,
              command=click_me())

b.pack()

win.mainloop()
