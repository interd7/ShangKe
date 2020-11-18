# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :001
# @Date     :2020/11/16 8:05 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd

df = pd.DataFrame({'ID':[1,2,3],'Name':['Tim','Vitor','Nick']})
df = df.set_index('ID')
# df.to_excel('/Users/inter.d/PycharmProjects/ShangKe/OpreateExcel/output.xlsx')
print(df)
print('Done!')

