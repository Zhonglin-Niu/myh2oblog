from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表
class UserInfo(AbstractUser):
    a = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = '用户'
