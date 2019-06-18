#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-16 14:28
# @Author  : 张江
# @Site    : 
# @File    : commonTools.py
# @Software: PyCharm
import time
import json


def requestJSON(func):
    def func_inner(*args,**kwargs):
        start_time = time.time()
        # 处理对应的参数
        print(args[0])
        print(kwargs)
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('run time is %s' %(stop_time - start_time))
        return res
    return func_inner
