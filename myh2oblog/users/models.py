from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表
class UserInfo(AbstractUser):

    class Meta:
        verbose_name_plural = '用户'
