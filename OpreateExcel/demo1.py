# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :demo1
# @Date     :2020/12/2 11:36 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd
df = pd.DataFrame(pd.read_excel('成绩单.xlsx', sheet_name="测验成绩"))
temp = df[["测验1", "测验2", "测验3"]]
df["平均分"] = temp.mean(axis=1)
df.to_excel('学生成绩单.xlsx',sheet_name='学生测验成绩单',index=False)
