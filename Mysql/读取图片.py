# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :读取图片
# @Date     :2020/12/9 11:56 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql
from PIL import Image
# 读取图片，存储到本地并显示
try:
    conn = pymysql.connect(host='localhost', port=3306,
                           database='dymtest', user='root', password='root1234',
                           charset='utf8')
    cursor = conn.cursor()
    # 查询数据库，读取图片字段
    cursor.execute("SELECT data FROM my_images where id=1")
    # 读取图片字段写入到本地
    filename = 'image.png'
    fout = open(filename, 'wb')
    fout.write(cursor.fetchone()[0])
    fout.close()
    cursor.close()
    conn.close()
    print('从数据库中读取 {} 成功'.format(filename))
# 显示图片
    img1 = Image.open(filename)
    img1.show()
except IOError as e:
    print(e)
    print('读取数据库中的图片失败')
