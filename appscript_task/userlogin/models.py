# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.IntegerField(null=True, blank=True)
    area = models.TextField(max_length=1000,null=True, blank=True)
    state = models.CharField(max_length=20,null=True, blank=True)
    city = models.CharField(max_length=20,null=True, blank=True)
    def __str__(self):
        return self.user.username
