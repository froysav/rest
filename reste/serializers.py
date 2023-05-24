from rest_framework.serializers import ModelSerializer, Serializer

from .models import Product, User, Category, ShoppingCard, Like, Color
from rest_framework import serializers


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    color = ColorSerializer

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)


class ProductSerializerForCard(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price', 'category')


class ProductLikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('product', 'user', 'date')


class ShoppingCardSerializer(ModelSerializer):
    class Meta:
        model = ShoppingCard
        fields = ('product', 'quantity', 'user', 'date')


class ShoppingCardForDetailSerializer(ModelSerializer):
    product = ProductSerializerForCard()

    class Meta:
        model = ShoppingCard
        fields = ('product', 'quantity')
