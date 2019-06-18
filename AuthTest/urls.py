#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 10:13
# @Author  : 张江
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from AuthTest import views

app_name = 'AuthTest'

urlpatterns = [
    url(r'^index/$', views.index,name='indexPage'),
    url(r'^login_success/$',views.login_success,name='login_success'),
    url(r'^auth_logout/$',views.auth_logout,name='auth_logout'),
]