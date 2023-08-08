# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 16:46
# @Author  : wwz18078
# @File    : middlewares.py
# @Software: PyCharm
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from account.jwt_utils import ArtJwt


class LoginCheck(MiddlewareMixin):
    def process_view(self, request, view, *args, **kwargs):
        login_exempt = getattr(view, "login_exempt", False)
        if login_exempt:
            return None
        try:
            http_auth = request.META.get("HTTP_AUTHORIZATION", '')
            access_token = http_auth.split()[1]
            data = ArtJwt().decode_token(access_token)
        except Exception:
            return HttpResponse(status=401)
        user_uid = data.get("data")
        request.is_authenticated = True
        request.user_uid = user_uid
        return None
