from django.contrib import admin

from reste.models import Product, User, Category, ShoppingCard, Like,Color

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(ShoppingCard)
admin.site.register(Like)
admin.site.register(Color)