# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :0909
# @Date     :2020/9/9 10:47 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from pypinyin import pinyin,slug,Style
print(slug("段益迈", separator=' ',style = Style.TONE))
print("段   益   迈")
# print("%.3f" % 3.1415926)
print(slug("春晓", separator=' ',style= Style.TONE))
print("《春  晓》")
print(slug("作者 孟浩然", separator=' ',style= Style.TONE))
print("作 者:     孟   浩   然")
print(slug("春眠不觉晓 处处闻啼鸟 ", separator=' ',style= Style.TONE))
print(" 春  眠  不  觉  晓,      处  处  闻  啼  鸟")
print(slug("夜来风雨声 花落知多少 ", separator=' ',style= Style.TONE))
print(" 夜  来  风  雨  声,      花  落  知  多  少")
