# -*- coding: utf-8 -*-
# @Time : 2022/1/29 21:34
# @Author : 风轻云
# @File : urls.py

from django.urls import path, re_path
from . import views

app_name = "api"
urlpatterns = [
    path('post_article/', views.PostArticleView.as_view(), name="postArticle"),
    re_path(r'edit_article/(?P<nid>\d+)', views.EditArticleView.as_view(), name='editArticle'),
]
