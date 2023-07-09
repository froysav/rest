from django.contrib import admin

from reste.models import Product, Category, ShoppingCard, Like, Color, Comment, Blog, Reviews,User

admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(ShoppingCard)
admin.site.register(Like)
admin.site.register(Color)
admin.site.register(Comment)
admin.site.register(Reviews)
