from django.db import models

# Create your models here.
from common.models import BaseModel

GENDER = (
    ('male', "男"),
    ('female', "女"),
    ('unknown', "未知"),
)


class User(BaseModel):
    """
    用户
    """
    user_uid = models.CharField(max_length=32, unique=True, blank=True, null=True, verbose_name="user_uid")
    username = models.CharField(max_length=64, blank=False, null=False, verbose_name="用户名")
    password = models.CharField(max_length=128, blank=False, null=False, verbose_name="密码")
    email = models.CharField(max_length=64, blank=True, null=True, verbose_name="邮箱")
    tel = models.CharField(max_length=128, blank=True, null=True, verbose_name="电话")
    sex = models.CharField(max_length=16, choices=GENDER, default="unknown", blank=True, null=True, verbose_name="性别")
    user_locked = models.BooleanField(default=False, verbose_name="是否锁定")

    class Meta:
        verbose_name = "用户表"


class UserLeader(BaseModel):
    """
    用户领导表
    """
    user = models.ForeignKey(User, to_field="user_uid", verbose_name="用户", related_name="user_leader_user",
                             on_delete=models.CASCADE)
    leader = models.ForeignKey(User, to_field="user_uid", verbose_name="领导", related_name="user_leader_leader",
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = "用户领导"


class Department(BaseModel):
    """
    部门表
    """
    code = models.CharField(max_length=64, verbose_name="code")
    name = models.CharField(max_length=64, verbose_name="部门名称")
    superior_department_id = models.IntegerField(blank=True, null=True, verbose_name="上级部门ID")
    department_path = models.CharField(max_length=128, blank=True, null=True, verbose_name="部门路径编码")

    class Meta:
        verbose_name = "部门"
