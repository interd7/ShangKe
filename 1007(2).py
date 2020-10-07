# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1007(2)
# @Date     :2020/10/7 11:58 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# -*- coding: utf-8 -*-
import openpyxl
import random

myList = []
#  1. 读取excel文档
wb = openpyxl.load_workbook(r'/Users/fushengyuanwuhui/Downloads/计科18级学生名单.xlsx')
#  2. 获取工作表中
sheet = wb[wb.sheetnames[0]]
for row in sheet.rows:
    list1 = []
    for cell in row:
        list1.append(cell.value)
    myList.append(list1)

set1 = set()
while True:
    c1 = random.randint(1, 80)
    set1.add(c1)
    if (len(set1) == 20):
        break

k = 0
for j in set1:
    print(myList[j],end="\t")
    k += 1
    if (k == 5):
        print()
        k = 0

