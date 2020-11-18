# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :kanshuzi
# @Date     :2020/11/18 11:57 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pytesseract
from PIL import Image
captcha = Image.open("/Users/inter.d/PycharmProjects/ShangKe/MoniDenglu/code.gif")
check_code = pytesseract.image_to_string(captcha)
print(check_code)
