# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :except1
# @Date     :2020/12/9 8:39 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# 除数不能为0

try:    # 捕获异常
    x = int(input("请输入一个数："))

    y = int(input("请输入一个数："))

    z = x / y

    print("{}/{}={}".format(x, y, z))

except ZeroDivisionError:

    # 处理除0异常

    print("\n出错了，除数不能为0！")

except ValueError as e:

    # 处理ValueError异常

    print("输入数据类型错误：", e)

# 输出错误原因
else:

    print("没有发生任何异常！")

finally:

    print("我始终在这")
