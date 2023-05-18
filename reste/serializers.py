from rest_framework.serializers import ModelSerializer, Serializer

from .models import Product, Detail, User, Category
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class Detailserializer(ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
