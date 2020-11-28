from tkinter import *

# 构造一个窗体
from tkinter import messagebox

window = Tk()
# 设置标题
window.title("求圆形的面积")
# 设置窗口大小
window.geometry("400x300")
# 构造组件，并按表格布局放置窗体上面
# 标签
Label(window, text="半径：").grid(row=0, column=0)
# 声明变量
var_r = StringVar()
var_area = StringVar()
# 输入框
entry_r = Entry(window, width=20, bg="lightblue", textvariable=var_r)
entry_r.grid(row=0, column=1)
# 标签
Label(window, text="面积：").grid(row=1, column=0)
# 输入框
entry_area = Entry(window, width=20, bg="lightblue", textvariable=var_area)
entry_area.grid(row=1, column=1)
# 按钮
Button(window, text="退出", command=window.quit).grid(row=2, column=0)
def myfunction():
    r = float(var_r.get())
    messagebox.showinfo(title='Hi', message='你好！'+str(r))
    var_area.set(3.14 * r * r )
    pass

Button(window, text="计算", command=myfunction).grid(row=2, column=1)
# 显示窗体
window.mainloop()
