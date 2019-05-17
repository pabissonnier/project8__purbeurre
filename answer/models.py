from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=500, null=True)
    nutriscore = models.CharField(max_length=1, null=True)
    ingredients = models.CharField(max_length=500, null=True)
    shops = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    picture = models.URLField()

    def __str__(self):
        return self.name


class UserList(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    nutriscore = models.CharField(max_length=1, null=True)
    ingredients = models.CharField(max_length=500, null=True)
    shops = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    picture = models.URLField()

    def __str__(self):
        return self.name
