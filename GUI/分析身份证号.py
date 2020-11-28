# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :分析身份证号
# @Date     :2020/11/25 11:46 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# -*- coding: utf-8 -*-


import tkinter

window = tkinter.Tk()
window.title("身份证号解析")
window.geometry("800x500")
c = {'11': '北京市', '12': '天津市', '13': '河北省', '14': '山西省',
     '15': '内蒙古自治区', '22': '吉林省', '23': '黑龙江省', '31': '上海市',
     '32': '江苏省', '33': '浙江省', '35': '福建省', '36': '江西省', '37': '山东省',
     '41': '河南省', '42': '湖北省', '44': '广东省', '45': '广西壮族自治', '46': '海南省',
     '50': '重庆市', '51': '四川省', '53': '云南省', '54': '西藏自治区', '61': '陕西省', '62': '甘肃省',
     '63': '青海省', '65': '新疆维吾尔自治区', '71': '台湾省', '81': '香港', '82': '澳门'}

var = tkinter.StringVar()
var1 = tkinter.StringVar()
var2 = tkinter.StringVar()
var3 = tkinter.StringVar()
label_1 = tkinter.Label(window, text="身份证号")
label_1.grid(row=0, column=0)
entry1 = tkinter.Entry(window, textvariable=var,bg = 'Yellow')
entry1.grid(row=0, column=1)


def click_me():
    s = var.get()
    var1.set(c[s[0:2]])
    var2.set(s[6:10] + "年" + s[10:12] + "月" + s[12:14] + "日")
    if (int(s[16]) % 2 == 0):
        var3.set("女")
    else:
        var3.set("男")
    pass


btn_1 = tkinter.Button(window, text="开始解析", command=click_me)
btn_1.grid(row=0, column=2)
label_3 = tkinter.Label(window, textvariable=var1)
label_3.grid(row=1, column=1)
label_4 = tkinter.Label(window, textvariable=var2)
label_4.grid(row=2, column=1)
label_5 = tkinter.Label(window, textvariable=var3)
label_5.grid(row=3, column=1)

window.mainloop()
