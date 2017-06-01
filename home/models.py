from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member(User):
    name = models.CharField(max_length=100)
    pwd = models.CharField(default='',max_length=20)
    role = models.CharField(default='Customer',max_length=20)
    mobile = models.CharField('Mobile No.',default='',max_length=11)
    email_id = models.CharField('Email-id',max_length=200)

    def __unicode__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return str(self.name)


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(default='/media/products/no_image.jpg')
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return str(self.name)




