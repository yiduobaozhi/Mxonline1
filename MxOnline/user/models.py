# encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Userprofile(AbstractUser):
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    nick_name=models.CharField(max_length=50,default='')
    birthday=models.DateField(null=True,blank=True)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=5,default='female')
    address=models.CharField(max_length=100,default='')
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(default='/image/default.png',upload_to='image/%Y/%m',max_length=100)

    def __str__(self):
        return self.username        # username为继承自abstractuser
