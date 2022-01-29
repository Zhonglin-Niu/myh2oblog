# -*- coding: utf-8 -*-
# @Time : 2022/1/28 22:34
# @Author : 风轻云
# @File : my_tags.py
from django import template

register = template.Library()


@register.filter
def cut(value, change):
    """Removes all values of arg from the given string"""
    return value.replace(change, '')


@register.filter
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.simple_tag
def banner(name):
    return name
