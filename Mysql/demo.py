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

db = pymysql.connect(
    host='localhost',
    port=3306,
    database='dymtest',
    user='root',
    password='root1234',
    charset='utf8'
)

cursor  = db.cursor()
try:
    cursor.execute("create table students_info(id int not null primary key ,sno varchar(20) not null,sname varchar(20) not null,gender varchar(2) default '男' null,age int null);")
    db.commit()
    print("Done!")
except:
    print("Error!")
    db.rollback()

db.close()

