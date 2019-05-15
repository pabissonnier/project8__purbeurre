from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    nutriscore = models.CharField(max_length=1, null=True)
    ingredients = models.CharField(max_length=500, null=True)
    shops = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=200, null=True)
    picture = models.URLField()

    def __str__(self):
        return self.name


class User(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
