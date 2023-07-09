from contextvars import Token
from sqlite3 import IntegrityError
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
import datetime
from rest import settings
from .models import Product, User, Category, ShoppingCard, Color, Comment, Blog, Reviews, Like
from .serializers import ProductSerializer, CategorySerializer, ShoppingCardForDetailSerializer, ShoppingCardSerializer, \
    ProductLikeSerializer, ColorSerializer, CommentSerializer, LargeResultsSetPagination, EmailSerializer, \
    BlogSerializer, ReviewSerializer
from .tasks import send_email
from rest_framework import status, generics, filters
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


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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

    # def post(self, request):
    #     product_data = ProductSerializer(data=request.data)
    #     product_data.is_valid(raise_exception=True)
    #     product_data.save()
    #     current_date = datetime.datetime.now()
    #     finish_date = current_date + datetime.timedelta(minutes=1)
    #     print("Finish date:", finish_date)
    #     send_email.delay('roncrist5575@gmail.com', 'We have added a new product check our website')
    #     return Response(status=201)
    def post(self, request):
        product_data = ProductSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product = product_data.save()

        current_date = datetime.datetime.now()
        finish_date = current_date + datetime.timedelta(minutes=1)
        print("Finish date:", finish_date)

        # Schedule the email task to be executed after 1 minute
        send_email.apply_async(args=['roncrist5575@gmail.com', 'We have added a new product. Check our website'],
                                    eta=finish_date)

        return Response(status=201)


class CategorylistAPIView(APIView):

    def get(self, request):
        products = Category.objects.all()
        products_data = CategorySerializer(products, many=True)
        return Response(products_data.data)


# class LikelistAPIView(APIView):
#
#     def get(self, request):
#         products = Like.objects.all()
#         products_data = ProductLikeSerializer(products, many=True)
#         return Response(products_data.data)

class LikelistAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        products = Like.objects.filter(user=user)
        products_data = ProductLikeSerializer(products, many=True)
        return Response(products_data.data)


class CardlistAPIView(APIView):

    def get(self, request):
        products = ShoppingCard.objects.all()
        products_data = ShoppingCardSerializer(products, many=True)
        return Response(products_data.data)


class BlogAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Blog.objects.all()
        products_data = BlogSerializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        product_data = BlogSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)

    def delete(self, request, pk):
        try:
            product = Blog.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product.delete()
        return Response(status=204)


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


class BlogDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(product)
            return Response(serializer.data)

        except:
            return Response('This does not exist')

    def put(self, request, pk):
        try:
            product = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(status=404)
        product_data = BlogSerializer(product, data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data)


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        except:
            return Response('This does not exist')


class BillingsRecordsView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = LargeResultsSetPagination


# class ReviewsAPIView(APIView):
#     def post(self, request):
#         reviews = Reviews.objects.all()
#         reviews_serializers = ReviewSerializer(reviews)
#         return Response(status=201)

class ReviewsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_data = ReviewSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)

    def get(self, request):
        products = Reviews.objects.all()
        products_data = ReviewSerializer(products, many=True)
        return Response(products_data.data)


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

    def get(self, request):
        products = Like.objects.all()
        products_data = ProductLikeSerializer(products, many=True)
        return Response(products_data.data)

    def delete(self, request):
        user_id = request.user.id
        like = Like.objects.filter(user_id=user_id).first()
        if like:
            like.delete()
            return Response(status=204)
        else:
            return Response(status=404)


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


class BillingRecordsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LargeResultsSetPagination


class SendMail(APIView):
    def post(self, request):
        try:
            serializer = EmailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            message = 'Test message'
            send_email.delay(email, message)
        except Exception as e:
            return Response({'success': False, 'message': f'{e}'})
        return Response({'success': True, 'message': 'Sent'})


# class SearchAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name']
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         q = self.request.GET.get('q', None)
#         if q:
#             queryset = queryset.filter(name__icontains=q)
#         return queryset

class SearchAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category__name', 'price']

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', None)
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(category__name__icontains=q) |
                Q(price__icontains=q)
            )
        return queryset
