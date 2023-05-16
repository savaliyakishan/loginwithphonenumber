from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class User(AbstractUser):
    phone = models.CharField(max_length=255,db_column="Phone_Number",null=False,blank=False,unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS =[]
