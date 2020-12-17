# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :study
# @File     :demo
# @Date     :2020/12/9 9:00
# @Author   :段益迈
# @Email    :406203230
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql
# 1. 连接数据库，
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root1234',
    db='dymtest',
    charset='utf8',
    # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
# 2.使用cursor()方法获取操作游标
cursor = conn.cursor()
#获得版本号
cursor.execute('select version()')
data=cursor.fetchone()
print('数据库版本：%s'%data)
# 创建数据表，如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS test2")
# 创建数据表SQL语句
sql = """create table test2(
         student_num INT NOT NULL,primary key(student_num),
         name CHAR(10) NOT NULL,
         age INT,
         sex CHAR(1))
         """
# 使用execute方法执行SQL语句
cursor.execute(sql)
# 2). *********************插入数据****************************
#SQL 插入语句
sql='insert into test2(student_num,name,age,sex) value (%s,%s,%s,%s)'
data=(1,'张三',19,'男')
cursor.execute(sql,data)
conn.commit()

# # 3). **************************数据库更新*****************************
# # SQL 更新语句
sql = "update test2 set name=%s where student_num=1"
params=("小七")
cursor.execute(sql,params)
conn.commit()

sql1='insert into test2(student_num,name,age,sex) value (%s,%s,%s,%s)'
data=((2,'Anne',20,'女'),(3,'李四',19,''),(4,'王五',26,'男'),(5,'Lisa',18,'女'),(6,'Tom',30,''))
cursor.executemany(sql1,data)
conn.commit()
# 4). **************************数据库查询*****************************
sql= "select * from test2"
result = cursor.execute(sql)  # 默认不返回查询结果集， 返回数据记录数。
print(result)

#fetchone():获取下一个查询结果集
print(cursor.fetchone())
print(cursor.fetchone())
#
#每一次都让游标返回user表的开头
cursor.execute('select * from test2')
print(cursor.fetchone())
#print(cursor.fetchone())

#指针移动到最开始处
print("正在移动指针到最开始......")
cursor.scroll(0, 'absolute')  #指针无条件的从0开始
print(cursor.fetchone())
#fetchmany():获取制定个数查询结果集
print(cursor.fetchmany(3))

#fetchall():获取所有的查询结果
cursor.execute('select * from test2')
info = cursor.fetchall()
print(info)

# #rowcount():返回执行sql语句影响的行数，可以知道指针查询了几条数据
# cursor.execute('select * from test2')
# print(cursor.rowcount)
# print("")
# cursor.scroll(0, 'absolute')
# info = cursor.fetchone()  # 指针移动到最后
# print(info)
# cursor.scroll(2)
# print(cursor.fetchone())

#当刚开始使用absolute权限的指针时,将指针权限改成比他权限要小的指针时，将会报错
# cursor.execute('select * from test2')
# print("正在移动指针到第2个......")
# cursor.scroll(1, mode='relative')  #指针相对的从0，1，2开始，都可以
# print(cursor.fetchone())
#同理也是,当刚开始使用relative权限的指针时,将指针权限改成比他权限要小的指针时，将会报错
#cursor.scroll(1,'absolute')
#cursor.execute('select * from test2')
# cursor.scroll(1, mode='relative')
cursor.execute('select * from test2')
data1 = cursor.fetchall()
print("id name age gender")
for data in data1:
    for i in data:
        print(i,end="   ")
    print("\n")
# #rollback（）方法回滚当前游标的所有操作
# # 注：当且仅当你没有赋予指针权限时
# conn.rollback()
# print(cursor.fetchone())

# 5). **************************数据库删除*****************************
"""
#单删
sql = "DELETE FROM test2 WHERE student_num = 1;"
cursor.execute(sql)
conn.commit()
"""
#批量删除
# list=[2,4,6]
# cursor.executemany("delete from test2 where student_num=%s",list)
conn.commit()
