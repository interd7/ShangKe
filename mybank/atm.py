# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :atm
# @Date     :2020/10/21 10:00 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import time

from mybank.card import Card
from mybank.user import User
import random


class Atm:

    def __init__(self, all_users):
        self.all_users = all_users

    def creat_user(self):
        name = input("请输入姓名：")
        uid = input("请输入身份证号：")
        phone = input("请输入手机号：")
        prest_money = float(input("请输入预存金额："))
        if prest_money <= 0:
            print("预存款输入有误，开户失败")
            return -1
        pwd1 = input("请输入密码：")
        pwd2 = input("请再次输入密码：")
        if pwd1 != pwd2:
            print("两次密码输入不同......")
            return -1
        print("密码设置成功，请牢记密码")
        card_id = self.random_card_id()
        card = Card(card_id,pwd1, prest_money)
        user = User(name, uid, phone, card)
        self.all_users[card_id] = user
        print("您的开户已完成，请牢记开户账号：{}\n".format(card_id))
        time.sleep(5)

    def check_pwd(self, real_pwd):
        for i in range(3):
            tempPwd = input("请输入密码：")
            if tempPwd == real_pwd:
                return True
        return False

    def search_user(self):
        cardNum = input("请输入卡号：")
        user = self.all_users.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if user.card.card_lock:
            print("该卡已锁定！请解锁后重试！")
            return -1
        if not self.check_pwd(user.card.card_pwd):
            print("密码错误，该卡已锁定，请解锁后重试")
            user.card.card_lock = True
            return -1
        print("正在查询，请稍后......")
        time.sleep(1)
        print("账号:{},余额:{}".format(user.card.card_id, user.card.money))
        time.sleep(5)

    def get_money(self):
        cardNum = input("请输入卡号：")
        user = self.all_users.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if user.card.card_lock:
            print("该卡已锁定！请解锁后重试！")
            return -1
        if not self.check_pwd(user.card.card_pwd):
            print("密码错误，该卡已锁定，请解锁后重试")
            user.card.card_lock = True
            return -1
        amount = int(input("验证成功！请输入取款金额："))
        if amount > user.card.money:
            print("取款金额有误，取款失败！")
            return -1
        if amount < 0:
            print("取款金额有误，取款失败！")
            return -1
        user.card.money -= amount
        print("正在取款，请稍后......")
        time.sleep(1)
        print("您取款{}元，余额为{}元！".format(amount, user.card.money))
        time.sleep(5)
    def save_money(self):
        cardNum = input("请输入卡号：")
        user = self.all_users.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if user.card.card_lock:
            print("该卡已锁定！请解锁后重试！")
            return -1
        if not self.check_pwd(user.card.card_pwd):
            print("密码错误，该卡已锁定，请解锁后重试")
            user.card.card_lock = True
            return -1
        amount = int(input("验证成功！请输入存款金额："))
        if amount < 0:
            print("存款金额有误，存款失败！")
            return -1
        user.card.money += amount
        print("正在验钞，请稍后......")
        time.sleep(1)
        print("您存款{}元，最新余额为{}元！".format(amount, user.card.money))
        time.sleep(5)

    def transfer_money(self):
        cardNum = input("请输入卡号：")
        user = self.all_users.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if user.card.card_lock:
            print("该卡已锁定！请解锁后重试！")
            return -1
        if not self.check_pwd(user.card.card_pwd):
            print("密码错误，该卡已锁定，请解锁后重试")
            user.card.card_lock = True
            return -1
        amount = int(input("验证成功！请输入转账金额："))
        if amount > user.card.money or amount < 0:
            print("金额有误，转账失败！")
            return -1
        newCard = input("请输入转入账户：")
        newUser = self.all_users.get(newCard)
        if not newUser:
            print("该卡号不存在，转账失败！")
            return -1
        # 判断是否锁定
        if newUser.card.card_lock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1
        user.card.money -= amount
        newUser.card.money += amount
        time.sleep(1)
        print("转账成功，请稍后···")
        time.sleep(1)
        print("转账金额{}元，余额为{}元！".format(amount, user.card.money))
        time.sleep(5)

    def lock_card(self):
        cardNum = input("请输入卡号：")
        user = self.all_users.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if user.card.card_lock:
            print("该卡已锁定！请解锁后重试！")
            return -1
        if not self.check_pwd(user.card.card_pwd):
            print("密码错误，锁定失败！")
            return -1
        tempIdCard = input("请输入身份证号码：")
        if tempIdCard != user.id:
            print("身份证号有误，锁定失败")
            return -1
        user.card.card_lock = True
        print("锁定成功！")
    def unlock_card(self):
        cardNum = input("请输入卡号：")
        user = self.all_users.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败")
            return -1
        if not user.card.card_lock:
            print("该卡未被锁定，无需解锁！")
            return -1
        if not self.check_pwd(user.card.card_pwd):
            print("密码错误，解锁失败！")
            return -1
        tempIdCard = input("请输入身份证号码：")
        if tempIdCard != user.id:
            print("身份证号有误，解锁失败")
            return -1
        user.card.card_lock = False
        print("解锁成功！")

    def random_card_id(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord("0"), ord("9") + 1))
                str += ch
            # 判断是否重复
            if not self.all_users.get(str):                             # 这里是通过找一下原来的字典中是否有这个key，如果没有的话那么这个卡号就合法，前面要有个not，没有找到这个卡号那么我们创建这个卡号
                return str
