# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :demo
# @Date     :2020/12/9 9:00 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql
# hjl ID 172.18.2.128
db = pymysql.connect(
    host='localhost',
    port=3306,
    database='dymtest',
    user='root',
    password='root1234',
    charset='utf8'
)
# sql1 = "DROP TRIGGER delete_all38728127398123716473458324"
# sql2 = "select * from students_info"
# sql = """
# insert into students_info(id,sno,sname,gender,age) values (%s,%s,%s,%s,%s);
# """
# sql_update = "update students_info set sname = %s where sname = '段益迈2'"
# name_data = ("dymzs")
# sql_data = [('1','180809329','段益迈','男','18'),
# ('2','180809330','段益迈2','男','19'),
# ('3','180809331','段益迈3','男','20'),
# ('4','180809332','段益迈4','男','21'),
# ('5','180809333','段益迈5','男','22')]

# sql_delete = 'delete from students_info where sno = %s'
# delete_list = ["180809329","180809330","180809331"]
cursor  = db.cursor()
try:
    # cursor.execute(sql_update,name_data)
    # cursor.executemany(sql,sql_data)
    # cursor.executemany(sql_delete,delete_list)
    # data = cursor.fetchall()
    db.commit()
    print("Done!")
    # print(data)
except:
    print("Error!")
    db.rollback()
# finally:
#     print(sql_data[0])
db.close()

