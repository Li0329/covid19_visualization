from django.db import models

# Create your models here.
"""
    用户表包括:
    - 用户名
    - 密码
    - 邮箱地址
   来支撑基本的 ‘登录’ 与 ‘注册’操作 
"""


class UserInfo(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.username
