# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:Listbox 部件
# @Date     :2020/11/25 9:52 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from tkinter import *
# 创建窗口对象
window = Tk()
# 创建一个列表
language_list = ['python', 'java', 'c', 'javascript']
# 创建一个列表组件
lb_language = Listbox(window)

# 这里有一个 selectmode 选项，默认是 BROWSE（单选,拖动鼠标或方向键可以改变选项），
# SINGLE（纯粹单选），
# MULTIPLE（多选） lb_language = Listbox(window, selectmode=MULTIPLE)
# EXTENDED(多选，但要按住 shifu 或者 ctrl)

# 向列表框插入数据
for item in language_list:
    lb_language.insert(END, item)

# 向列表框插入数据
lb_language.insert(2, "php")
lb_language.insert(END, "go")
lb_language.insert(0, "sql")

# 删除列表框中数据
lb_language.delete(1)
lb_language.delete(first=0, last=2)
# lb_language.delete(0, END) # 清空列表
lb_language.pack() # 将列表框放置到主窗口中

def btn1_click():
    if lb_language.curselection():
        # value = lb_language.get(lb_language.curselection())
        value = lb_language.selection_get()
        print(value)
    else:
        print("请先选择一项！")

btn1 = Button(window, text="获取选中数据", command=btn1_click)
btn1.pack()


def btn2_click():
    print(lb_language.size())
    pass

btn2 = Button(window, text="获取列表框长度", command=btn2_click)
btn2.pack()

window.mainloop() # 进入消息循环
