from django.db import models

from django.db import models
from flask import request


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    with_price = models.IntegerField()
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.color


class Product(models.Model):
    sale = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image1 = models.ImageField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.title}'


class ShoppingCard(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Shopping Card'
        verbose_name_plural = 'Shopping Cards'

    def __str__(self):
        return self.product.title


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title


class Reviews(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)


    def __str__(self):
        return self.name


class Blog(models.Model):
    image = models.ImageField()
    about = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __str__(self):
        return self.about
