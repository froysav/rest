from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from flask import Flask, request
from .models import Product, Detail, User, Category
from .serializers import ProductSerializer, Detailserializer, CategorySerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer


class RegisterView(APIView):
    def get(self, request):
        products = User.objects.all()
        products_data = UserSerializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': '🟢 User registered successfully.'}, status=201)
        return Response(serializer.errors, status=400)


class Categori(APIView):
    def post(self, request):
        product_data = CategorySerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)

    def get(self, request):
        products = Category.objects.all()
        products_data = CategorySerializer(products, many=True)
        return Response(products_data.data)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': '🟢 Login successful.'}, status=200)
            return Response({'message': '🔴 Invalid credentials.'}, status=401)
        return Response(serializer.errors, status=400)


class ProductAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        products_data = ProductSerializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        product_data = ProductSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)


class DetailAPIView(APIView):
    def get(self, request):
        products = Detail.objects.all()
        products_data = Detailserializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        product_data = Detailserializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)


class ProductUpdateDeleteAPIView(APIView):

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product_data = ProductSerializer(product, data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data)

    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product_data = ProductSerializer(product, data=request.data, partial=True)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product.delete()
        return Response(status=204)
