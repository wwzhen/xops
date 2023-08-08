# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 13:48
# @Author  : wwz18078
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from account.views import LoginView, RegisterView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view())
]
