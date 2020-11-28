# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :案例:Frame 窗口部件
# @Date     :2020/11/25 10:31 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import tkinter as tk # 使用 Tkinter 前需要先导入

# 第 1 步，实例化 object，建立窗口 window
window = tk.Tk()

# 第 2 步，给窗口的可视化起名字
window.title('Frame 用法')

# 第 3 步，设定窗口的大小(长 * 宽)
window.geometry('500x300')

# 第 4 步，在图形界面上创建一个标签用以显示内容并放置
tk.Label(window, text='这个标签在 window 上', bg='red', font=('Arial', 16), fg="white").pack() # 和前面部件分开创建和放置不同，其实可以创建和放置一步完成

# 第 5 步，创建一个主 frame，长在主 window 窗口上
frame = tk.Frame(window)
frame.pack()

# 第 6 步，创建第二层框架 frame，长在主框架 frame 上面
frame_l = tk.Frame(frame) # 第二层 frame，左 frame，长在主 frame 上
frame_r = tk.Frame(frame) # 第二层 frame，右 frame，长在主 frame 上

frame_l.pack(side='left')
frame_r.pack(side='right')

# 第 7 步，创建三组标签，为第二层 frame 上面的内容，分为左区域和右区域，用不同颜色标识

tk.Label(frame_l, text='这个标签在 frame_l 上', bg='pink').pack()
tk.Label(frame_l, text='这个标签在 frame_l 上', bg='pink').pack()
tk.Label(frame_l, text='这个标签在 frame_l 上', bg='pink').pack()
tk.Label(frame_r, text='这个标签在 frame_r 上', bg='yellow').pack()
tk.Label(frame_r, text='这个标签在 frame_r 上', bg='yellow').pack()
tk.Label(frame_r, text='这个标签在 frame_r 上', bg='yellow').pack()

# 第 8 步，主窗口循环显示
window.mainloop()
