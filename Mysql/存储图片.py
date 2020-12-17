# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :插入图片
# @Date     :2020/12/9 11:48
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql
import sys

# 将图片写入数据库中
# 将图片内容读到img中
try:
    filename = "1.png"
    # filename = "2.jpeg"
    with open(filename, 'rb') as fin:
        img = fin.read()
    fin.close()
except IOError as e:
    print(e)
    sys.exit(1)
# 将img写入数据库
try:
    conn = pymysql.connect(host='localhost', port=3306,
                           database='dymtest', user='root', password='root1234',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO my_images(data) VALUES (_binary %s)", (img))
    conn.commit()
    cursor.close()
    conn.close()
    print('写入 {} 成功'.format(filename))
except pymysql.Error as e:
    print(e)
    print('写入失败')
