#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 16:35
# @Author  : 张江
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from FormsTest import views
urlpatterns = [
    url(r'^forms_index/',views.form_index()),
]