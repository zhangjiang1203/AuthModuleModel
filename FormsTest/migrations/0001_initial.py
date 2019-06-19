# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=8)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
