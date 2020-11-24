# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :T1
# @Date     :2020/11/14 10:53 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import numpy as np
import pandas as pd

# NumPy是用Python进行科学计算的基础软件包
# pandas是基于NumPy数组构建的,使数据预处理、清洗、分析工作变得更快更简单,
# pandas是专门为处理表格和混杂数据设计的

#  导入数据表
# df=pd.DataFrame(pd.read_csv('name.csv',header=1))
# df=pd.DataFrame(pd.read_excel('./Documents/回答汇总.xlsx'))
# print(df.values)
#  创建数据表
df = pd.DataFrame({"id": [1001, 1002, 1003, 1004, 1005, 1006],
                   "date": pd.date_range('20130102', periods=6),
                   "city": ['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age": [23, 44, 54, 32, 34, 32],
                   "category": ['100-A', '100-B', '110-A', '110-C', '210-A', '130-F'],
                   "price": [1200, np.nan, 2133, 5433, np.nan, 4432]})

#  数据表检查
#  数据维度
# 查看数据表的维度
# print(df.shape)

# 数据表信息
# print(df.info())

# 查看数据格式
# 查看数据表各列格式
# print(df.dtypes)

# 查看空值
# Isnull是Python中检验空值的函数，返回的结果是逻辑值，包含空值返回True，
# 不包含则返回False。可以对整个数据表进行检查，也可以单独对某一列进行空值检查。

# 检查数据空值
# print(df.isnull())


# 检查特定列空值
# print(df['price'].isnull())

# 查看唯一值 （删除重复项）
# 查看city列中的唯一值
# print(df['city'].unique())

# 查看数据表的值
# print(df.values)

# 查看列名称
# print(df.columns)

# 删除列
# df = df.drop('city',1)

# 查看前3行数据
# print(df.head(3))

# 查看最后3行
# print(df.tail(3))

# 数据表清洗
# 处理空值
# 删除数据表中含有空值的行
# print(df)
# df = df.dropna(how='any')
# print(df)

# 使用数字0填充数据表中空值
# print(df.fillna(value=0))

# 使用price均值对NA进行填充
# print(df['price'].fillna(df['price'].mean()))

# 清理空格
# 清除city字段中的字符空格
# print(df['city'])
# df['city']=df['city'].map(str.strip)
# print(df['city'])

# 大小写转换
# city列大小写转换
# print(df['city'])
# df['city']=df['city'].str.lower()
# print(df['city'])

# 更改数据格式
# print(df['age'].dtype)
# print(df['age'].astype('float'))

# 更改列名称
# df = df.rename(columns={'category': 'category-size'})
# print(df.columns)

# 删除重复值
# 删除后出现的重复值
# print(df['city'].drop_duplicates())

# 删除先出现的重复值
# print(df['city'].drop_duplicates(keep='last'))

# 数值修改及替换
# 数据替换
# print(df['city'].replace('SH', 'shanghai'))

# 数据处理
# 设置索引列
# df = df.set_index('id')
# print(df)
# df.to_excel('/Users/inter.d/PycharmProjects/ShangKe/OpreateExcel/excel_to_python.xlsx', sheet_name='mySheet')
# print('Done!')
# 排序（按索引，按数值）
# 按特定列的值排序
# df.sort_values(by=['age'])

# 按索引列排序
# df.sort_index()

# 数据提取
# 按标签提取(loc)
# 按索引提取单行的数值
# print(df.loc[3])

# 使用冒号可以限定提取数据的范围，冒号前面为开始的标签值，后面为结束的标签值。下面提取了0到5的数据行。
# 按索引提取区域行数值
# print(df.loc[0:5])

# 使用冒号限定提取数据的范围，冒号前面为空表示从0开始。
# 提取所有2013年1月4日以前的数据
# print(df.loc[:'2013-01-04'])

# 按位置提取(iloc)
# 使用iloc函数按位置对数据表中的数据进行提取，这里冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始。
# 使用iloc按位置区域提取数据
# 0～3行，0～2列
# print(df.iloc[:3, :2])


# iloc函数除了可以按区域提取数据，还可以按位置逐条提取，
# 前面方括号中的0,2,5表示数据所在行的位置，后面方括号中的数表示所在列的位置。
# print(df.iloc[[0, 2, 5], [4, 5]])

# 分类汇总
# Groupby是进行分类汇总的函数，使用方法很简单，制定要分组的列名称就可以，也可以同时制定多个列名称，
# groupby按列名称出现的顺序进行分组。同时要制定分组后的汇总方式，常见的是计数和求和两种。
# 对所有列进行计数汇总
# print(df.groupby('city').count())

# 对特定的ID列进行计数汇总
# print(df.groupby('city')['id'].count())

# 对两个字段进行汇总计数
# print(df.groupby(['city', 'price'])['id'].count())

# 除了计数和求和外，还可以对汇总后的数据同时按多个维度进行计算，
# 下面的代码中按城市对price字段进行汇总，并分别计算price的数量，总金额和平均金额。
# 对city字段进行汇总并计算price的合计和均值。
# print(df.groupby('city')['price'].agg([len, np.sum, np.mean]))

# 输出到excel格式
# df.to_excel('./Documents/OpreateExcel.xlsx', sheet_name='mySheet')

# 输出到CSV格式
# df.to_csv('excel_to_python.csv')
