# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :1012
# @Date     :2020/10/12 3:50 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import openpyxl
#1.读取excel文档
wb = openpyxl.load_workbook(r'/Users/inter.d/Downloads/计科18级学生名单.xlsx')
#2.获取工作表中
sheet = wb[wb.sheetnames[0]]
for row in sheet.rows:
    for cell in row:
      print(cell.value, end='\t')
    print('\n')
