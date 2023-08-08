# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 13:52
# @Author  : wwz18078
# @File    : jwt_utils.py
# @Software: PyCharm
from datetime import datetime, timedelta

import jwt


class ArtJwt:
    def __init__(self):
        self.sk = "art@123"
        self.token_dict = {
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(hours=2),
        }
        self.sign = "HS256"

    def generate_token(self, data):
        self.token_dict.update(data=data)
        jwt_token = jwt.encode(self.token_dict, self.sk, algorithm=self.sign)
        return jwt_token.decode("ascii")

    def decode_token(self, jwt_token):
        data = jwt.decode(jwt_token, self.sk, algorithms=[self.sign])
        return data

    def token_validate(self, access_token):
        try:
            jwt.decode(access_token, self.sk, algorithms=[self.sign])
            return True
        except Exception:
            return False


if __name__ == '__main__':
    token = ArtJwt().generate_token("zhangsan")
    data = ArtJwt().decode_token(token)
    print(data)
