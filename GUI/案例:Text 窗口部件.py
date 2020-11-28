import tkinter as tk  # 使用 Tkinter 前需要先导入

# 第 1 步，实例化 object，建立窗口 window
window = tk.Tk()

# 第 2 步，给窗口的可视化起名字
window.title('Text 部件用法')

# 第 3 步，设定窗口的大小(长 * 宽)
window.geometry('500x300')

# 第 4 步，在图形界面上设定输入框控件 entry 框并放置
txt1 = tk.Entry(window, show=None)  # 显示成明文形式
txt1.pack()


# 第 5 步，定义两个触发事件时的函数 insert_point 和 insert_end（注意：因为 Python 的执行顺序是从上往下,所以函数一定要放在按钮的上面）
def insert_point():  # 在鼠标焦点处插入输入内容
    var = txt1.get()
    txt2.insert('insert', var)


def insert_end():  # 在文本框内容最后接着插入输入内容
    var = txt1.get()
    txt2.insert('end', var)


# 第 6 步，创建并放置两个按钮分别触发两种情况
btn1 = tk.Button(window, text='光标处插入', width=10,
                 height=2, command=insert_point)
btn1.pack()
btn2 = tk.Button(window, text='文本末尾插入', width=10,
                 height=2, command=insert_end)
btn2.pack()

# 第 7 步，创建并放置一个多行文本框 text 用以显示，指定 height=3 为文本框是三个字符高度
txt2 = tk.Text(window, height=3)
txt2.pack()

# 第 8 步，主窗口循环显示
window.mainloop()
