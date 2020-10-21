# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :my_main
# @Date     :2020/10/21 10:00 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import time
from mybank.admin import Admin
from mybank.atm import Atm


class HomePage:
    def __init__(self):
        self.all_user_id = {}
        self.atm = Atm(self.all_user_id)
        self.admin = Admin()

    def save_user(self):
        self.all_user_id.update(self.atm.all_users)
        print("数据存盘成功")

    def main(self):
        self.admin.print_admin_view()
        resL = self.admin.admin_option()
        if not resL:
            while True:
                self.admin.print_sys_function_view()
                option = input("请输入您的操作：")
                if option not in ("1", "2", "3", "4", "5",
                                  "6", "7", "8", "s", "Q", "q"):
                    print("输入操作项有误，请仔细确认")
                    time.sleep(1)
                if option == "1":
                    self.atm.creat_user()
                elif option == "2":
                    self.atm.search_user()
                elif option == "3":
                    self.atm.get_money()
                elif option == "4":
                    self.atm.save_money()
                elif option == "5":
                    self.atm.transfer_money()
                elif option == "6":
                    self.atm.lock_card()
                elif option == "7":
                    self.atm.unlock_card()
                elif option == "q":
                    print("退出")


if __name__ == "__main__":
    HomePage().main()
