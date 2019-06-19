from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.

# 使用auth组件的抽象类作为基类
class UserInfo(models.Model):
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.username