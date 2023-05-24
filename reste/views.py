from sqlite3 import IntegrityError

from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from flask import Flask, request
from .models import Product, User, Category, ShoppingCard,Color
from .serializers import ProductSerializer, CategorySerializer, ShoppingCardForDetailSerializer, ShoppingCardSerializer, \
    ProductLikeSerializer,ColorSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer


# class RegisterView(APIView):
#     def get(self, request):
#         products = User.objects.all()
#         products_data = UserSerializer(products, many=True)
#         return Response(products_data.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'message': '🟢 User registered successfully.'}, status=201)
#         return Response(serializer.errors, status=400)


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


class ColorsAPIView(APIView):
    def post(self, request):
        product_data = ColorSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)

    def get(self, request):
        products = Color.objects.all()
        products_data = ColorSerializer(products, many=True)
        return Response(products_data.data)


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


# class Detail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = ()

class Detail(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except:
            return Response('This does not exist')


class AddToShoppingCardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.data._mutable = True
        request.data['user'] = request.user.id
        serializer = ShoppingCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=201)


class LikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.data._mutable = True
        request.data['user'] = request.user.id
        serializer = ProductLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=201)


class UserShoppingCardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_products = ShoppingCard.objects.filter(user=request.user)
        serializer = ShoppingCardForDetailSerializer(user_products, many=True)
        summ = 0
        for element in serializer.data:
            summ += element['product']['price'] * element['quantity']
        data = {
            'data': serializer.data,
            'summ': summ
        }
        return Response(data)


class DeleteFromCardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            ShoppingCard.objects.get(Q(pk=pk), Q(user=request.user)).delete()
        except ShoppingCard.DoesNotExist:
            return Response({'message': 'Bunday mahsulot mavjud emas'})
        return Response(status=204)
