# -*- coding: utf-8 -*-
# @Time : 2022/1/29 21:42
# @Author : 风轻云
# @File : middleware.py

from django.utils.deprecation import MiddlewareMixin
import json


class HugAxios(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and request.META.get("CONTENT_TYPE") == 'application/json':
            request.data = json.loads(request.body)

    def process_response(self, request, response):
        return response
