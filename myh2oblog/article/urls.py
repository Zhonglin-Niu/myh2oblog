# -*- coding: utf-8 -*-
# @Time : 2022/1/28 17:08
# @Author : 风轻云
# @File : urls.py

from django.urls import path
from . import views

app_name = "article"
urlpatterns = [
    path('', views.index, name="index"),
]
