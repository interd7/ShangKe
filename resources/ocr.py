# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :ocr
# @Date     :2020/11/4 10:17 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pytesseract
from PIL import Image
# 直接识别

captcha = Image.open("/pa/3.png")

check_code = pytesseract.image_to_string(captcha)

print(check_code)
