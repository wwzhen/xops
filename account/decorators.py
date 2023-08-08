# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 18:01
# @Author  : wwz18078
# @File    : decorators.py
# @Software: PyCharm
from functools import wraps


def login_exempt(view_func):
    """
    登录装饰器
    :param view_func:
    :return:
    """

    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)

    wrapped_view.login_exempt = True
    return wraps(view_func)(wrapped_view)
