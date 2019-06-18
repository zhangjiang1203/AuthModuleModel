from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    uid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username
