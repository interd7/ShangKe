# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :admin
# @Date     :2020/10/21 10:00 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import time


class Admin:
    admin_account = '1'
    adm_pwd = '1'

    def print_admin_view(self):
        print("******************************")
        print("***                        ***")
        print("***                        ***")
        print("***      欢迎登录银行系统     ***")
        print("***                        ***")
        print("***                        ***")
        print("******************************")

    def print_sys_function_view(self):
        print("1.开户")
        print("2.查询")
        print("3.取款")
        print("4.存款")
        print("5.转账")
        print("6.锁定")
        print("7.解锁")
        print("Q.退出")

    def admin_option(self):
        input_admin_account = input("请输入管理员账号：")
        input_adm_pwd =  input("请输入管理员密码：")
        if input_admin_account == self.admin_account and input_adm_pwd == self.adm_pwd:
            # self.print_sys_function_view()
            pass
        else:
            print("账号密码错误！")
            return -1
        print("操作成功，请稍后......")
        time.sleep(2)
        return 0
