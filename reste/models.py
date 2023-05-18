from django.db import models

from django.db import models
from flask import request


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    sale = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=100)
    image1 = models.ImageField()
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(null=True)
    image5 = models.ImageField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Detail(models.Model):
    sale = models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100)
    image1 = models.ImageField()
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(null=True)
    image5 = models.ImageField(null=True)
    gos = models.IntegerField()

    def __str__(self):
        return self.sale


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
