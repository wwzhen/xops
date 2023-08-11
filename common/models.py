# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 13:16
# @Author  : wwz18078
# @File    : models.py
# @Software: PyCharm
from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=0)  # 返回状态是未删除的记录


class BaseModel(models.Model):
    """
    公共BaseModel
    """
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_deleted = models.BooleanField(default=0, verbose_name="删除标记位")

    objects = BaseManager()

    class Meta:
        abstract = True
