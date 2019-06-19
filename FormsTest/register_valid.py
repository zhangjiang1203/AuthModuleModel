#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-19 16:55
# @Author  : 张江
# @Site    : 
# @File    : register_valid.py
# @Software: PyCharm
'''forms组件'''
'''
1.数据校验
2.渲染页面
3.渲染错误信息
4.局部和全局的钩子函数
5.使用css的样式
'''
from FormsTest import models
#1.写一个类继承自forms
from django.core.exceptions import ValidationError #抛出异常处理
from django import forms
from django.forms import widgets
from django.forms import Form
import re

#自定义校验规则
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class RegisterForms(Form):
    # 2.编写校验的字段,该字段就是html页面上提交数据上传的字段
    # label就是类似于一个占位，如果没有传label，默认取对应字段展示
    '''field中对应的属性和释义
    required=True,               是否是必须验证,默认为True
    widget=None,                 HTML插件，添加类名，设置placeholder等等
    label=None,                  用于生成Label标签或显示内容
    initial=None,                初始值
    help_text='',                帮助信息(在标签旁边显示)
    error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
    validators=[],               自定义验证规则
    localize=False,              是否支持本地化
    disabled=False,              是否可以编辑
    label_suffix=None            Label内容后缀
    '''
    name = forms.CharField(min_length=3,max_length=8,
                           label="用户名",
                           widget=widgets.PasswordInput(attrs={'class': 'form-control',
                                                               'placeholder': '请输入名称(3-8字符)'}),
                           error_messages={'min_length':'用户名最少为3位',
                                           'max_length':'用户名最多8位',
                                           'required':'名称不能为空'})

    pwd = forms.CharField(min_length=3, max_length=20,
                          label='请输入密码',
                          widget=widgets.PasswordInput(attrs={'class':'form-control',
                                                              'placeholder':'请输入密码(6-20字符)'}),
                          error_messages={'min_length':'密码最少为3位',
                                          'max_length':'密码最多20位',
                                          'required':'密码不能为空'})

    re_pwd = forms.CharField(min_length=3, max_length=20,
                             label='请确认密码',
                             widget=widgets.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': '请确认密码'}),
                             error_messages={'min_length':'密码最少为3位',
                                             'max_length':'密码最多20位',
                                             'required':'密码不能为空'})

    phone = forms.CharField(label="请输入手机号码",
                            validators=[mobile_validate,],
                            widget=widgets.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': '请输入手机号码'}),
                            error_messages={'placerholder': '请输入手机号码'})

    email = forms.EmailField(label='请输入邮箱',required=False,
                             widget=widgets.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': '请输入邮箱'}),
                             error_messages={'invalid':'格式不合法',
                                             'max_length':'密码最多20位'})

    # 对于多传的字段不会出错，cleaned_data中不包含多传的字段
    # 少传的字段会报错，相当于对应的字段没有值
    # 3在对应的view视图中操作

    # 局部钩子函数(某个字段，自定义的规则，数据库是否存在，以什么开头)
    # 方法名必须为:clean_字段名
    def clean_name(self):
        #获取到当前对象，是cleaned_data之后的数据
        name = self.cleaned_data.get('name')
        if name.startswith('sb'):
            #以sb开头了返回错误信息,禁止使用sb开头的用户名
            raise ValidationError('不能以sb开头')
        user = models.UserInfo.objects.filter(username=name).first()
        if user:
            raise ValidationError('用户名已存在')
        return name


    #全局钩子，校验两次密码是否相同等
    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            return ValidationError('两次密码不一致')
