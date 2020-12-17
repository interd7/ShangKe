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
import numpy as np
data = {
    '姓名': ['张三', '李四', '王五', '赵六', '史七'],
    '性别': ['男', '女', '女', '男', '男'],
    '年龄': [18, 21, 25, 32, 29]
}
# 使用字典构建DataFrame对象
df = pd.DataFrame(data, index=['one', 'two', 'three', 'four', 'five'],columns=['姓名', '性别', '年龄'])
df["姓名"] = ['z3', 'l4', 'w5', 'z6', 's7']
df["高数"] = [89, 98, 50, 70, 85]
df["英语"] = [77, 88, 99, 66, 55]
df.insert(2,'python',[99,88,77,55,66])
print(df)
df = df.append(pd.DataFrame([['Julia','女',100,18,88,99],
                             ['ww','女',100,18,88,99]
                             ],
                            index=['aa','bb'],columns=['姓名','性别','年龄','python','高数','英语']))
print(df)

temp = df[['python','高数','英语']]
df['平均分'] = temp.mean(axis=1)
print(df)
