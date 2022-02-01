# -*- coding: utf-8 -*-
# @Time : 2022/1/28 22:34
# @Author : 风轻云
# @File : my_tags.py
from django import template
from article.models import Tags, Categories, Articles

register = template.Library()


@register.filter
def cut(value, change):
    """Removes all values of arg from the given string"""
    return value.replace(change, '')


@register.filter
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.inclusion_tag('my_tags/tag_cloud.html')
def tag_cloud():
    tags = Tags.objects.all()
    return locals()


@register.inclusion_tag('my_tags/category_cloud.html')
def category_cloud():
    categories = Categories.objects.all()
    for category in categories:
        category.number = Articles.objects.filter(category=category).count()
    return locals()
