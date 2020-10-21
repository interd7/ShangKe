# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :card
# @Date     :2020/10/21 10:00 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
class Card:
    def __init__(self, card_id, card_pwd, money):
        self.card_id = card_id
        self.card_pwd = card_pwd
        self.money = money
        self.card_lock = False
