#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 14:00
# @Author  : 张江
# @Site    : 
# @File    : CustomMiddleModule.py
# @Software: PyCharm

#添加自己的中间件

from django.utils.deprecation import MiddlewareMixin

# 可以在中间件中添加用户认证和登录设置等信息
class CustomMiddle(MiddlewareMixin):
    def process_request(self, request):
        print('自定义中间件请求',request)

    def process_response(self, request, response):
        print('自定义中间件响应',request,response)
        return response