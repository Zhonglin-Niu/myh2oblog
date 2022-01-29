# -*- coding: utf-8 -*-
# @Time : 2022/1/28 17:08
# @Author : 风轻云
# @File : urls.py

from django.urls import path, re_path
from . import views

app_name = "article"
urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^article/(?P<nid>\d+)', views.article_detail, name="arti_detail"),
]
