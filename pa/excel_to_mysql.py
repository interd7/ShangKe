# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :excel_to_mysql
# @Date     :2020/11/18 7:14 下午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pandas as pd
from sqlalchemy import create_engine

# df = pd.read_excel("学生信息表.xls")
df1 = pd.read_excel("xsxxb1.xls")

engine = create_engine("mysql+mysqlconnector://root:root1234@127.0.0.1:3306/dymtest",echo=False)

# df.to_sql(name='student',con=engine,if_exists='replace')

df1.to_sql(name='xsxxb1',con=engine,if_exists='replace',index='id')

print(engine.execute("show create table xsxxb1").first()[1])
# 显示插入表的语句
# print(engine.execute("show create table Tbb").first()[1])
# 统计多少行
# print(engine.execute("select count(1) from Tbb").first())
# 输出前5行
# print(engine.execute("select * from Tbb limit 5").fetchall())
# print(df.head(10))
# df.index.name = "id"
# df.to_excel("/Users/inter.d/PycharmProjects/ShangKe/pa/学生信息表.xls")
