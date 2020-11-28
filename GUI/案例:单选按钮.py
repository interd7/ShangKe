# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:单选按钮
# @Date     :2020/11/25 9:47 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter
window = tkinter.Tk()
window.title("单选按钮用法")
window.geometry("300x200+10+20")
# 创建 lable 标签
lb = tkinter.Label(window, text='请选择您的性别：', fg='blue')
lb.pack()
# 定义选择单选按钮后执行的函数
def func():
    mg = ''
    if r.get() == 1:
        mg += '男'
    else:
        mg += '女'
    text.delete(0.0, tkinter.END)
    text.insert('insert', mg)

# 创建单选项
r = tkinter.IntVar()
r.set(2) # 设置女被选中
male_select = tkinter.Radiobutton(window, text='男', value=1, variable=r, command=func)
male_select.pack()
female_select = tkinter.Radiobutton(window, text='女', value=2, variable=r, command=func)
female_select.pack()
# 创建文本框
text = tkinter.Text(window, width=30, height=3)
text.pack()
window.mainloop()
