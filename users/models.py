# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class UserList(models.Model):
    name = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=1000, null=True)
    nutriscore = models.CharField(max_length=1, null=True)
    ingredients = models.CharField(max_length=5000, null=True)
    shops = models.CharField(max_length=1000, null=True)
    link = models.CharField(max_length=1000, null=True, unique=True)
    picture = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name