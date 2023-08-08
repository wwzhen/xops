# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 12:29
# @Author  : wwz
# @File    : develop.py
# @Software: PyCharm

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xops',
        'USER': 'root',
        'PASSWORD': 'aaaaaa',
        "HOST": "8.130.45.165",
        'PORT': '3306',
        'CHARSET': 'utf8',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
    }
}
