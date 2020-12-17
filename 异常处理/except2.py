# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :except2
# @Date     :2020/12/9 8:48 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""


def division():
    x = input("请输入一个数：")
    y = input("请输入一个数：")
    if not x.isdigit() or not y.isdigit():
        raise ValueError("除法运算，操作数不是数值！")
    else:
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("除数不能为0！")
        else:
            z = x / y
            print("{}/{}={}".format(x, y, z))


if __name__ == '__main__':
    try:
        # 捕获异常
        division()
    # 调用分苹果的函数
    except ZeroDivisionError as e:
        # 处理ZeroDivisionError异常
        print("出错了，", e)
    except ValueError as e:
        # ValueError
        print("出错了，", e)
