# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 13:43
# @Author  : wwz18078
# @File    : services.py
# @Software: PyCharm
import re

from account.jwt_utils import ArtJwt
from account.models import User


# from common.encrypt import decrypt


class Register:

    @classmethod
    def register(cls, user_info: dict):
        """
        注册
        :param user_info:
        :return:
        """
        user_uid = user_info.get("user_uid")
        password = user_info.get("password")
        if not user_uid:
            raise Exception(f"用户名{user_uid}不能为空")
        cls.check_password_strength(password)
        user = User.objects.filter(user_uid=user_uid).first()
        if user:
            raise Exception(f"用户uid:{user_uid}已存在")
        # todo 密码加密存储
        # password = decrypt(password)
        User.objects.create(**user_info)

    @staticmethod
    def check_password_strength(password, password_level=1):
        score = 0
        length = len(password)
        if length > 12:
            score += 3
        elif length > 8:
            score += 2
        elif length > 6:
            score += 1

        lower = re.search('[a-z]', password) is not None
        upper = re.search('[A-Z]', password) is not None
        if lower and upper:
            score += 2

        numbers = re.search('[0-9]', password) is not None
        if numbers:
            score += 3

        special = re.search('[^A-Za-z0-9]', password) is not None
        if special:
            score += 3

        if score < 4:
            print("The password is weak")
        elif score < 8:
            print("The password is medium strength")
        else:
            print("The password is strong")

        if score < password_level:
            raise Exception(f"密码强度过低，请重新输入密码")


class Login:

    @classmethod
    def login(cls, user_uid, password):
        """
        登录
        :param user_uid:
        :param password:
        :return:
        """
        if not user_uid:
            raise Exception(f"用户名{user_uid}不能为空")
        user = User.objects.filter(user_uid=user_uid).first()
        if not user:
            raise Exception(f"用户{user_uid}不存在")
        if user.password != password:
            raise Exception(f"密码错误")
        jwt_token = ArtJwt(username=user_uid).generate_token()
        return jwt_token
