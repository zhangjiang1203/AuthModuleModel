#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 11:33
# @Author  : 张江
# @Site    : 
# @File    : commonTools.py
# @Software: PyCharm


import json,time
# 引入静态库中的文件
def requestJSON(func):
    def func_inner(*args,**kwargs):
        start_time = time.time()
        # 处理对应的参数
        req = args[0]
        if req.method == "POST":
            if req.POST:
                pass
            else:
                if req.body:
                    req.POST = json.loads(req.body)
            name = req.POST.get('name')
            pwd = req.POST.get('pwd')
            print(name,pwd)
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('run time is %s' %(stop_time - start_time))
        return res
    return func_inner