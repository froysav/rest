from amqp import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, Serializer, EmailField
from .models import Product, User, ShoppingCard, Like, Color, Comment, Blog, Reviews, Category
from rest_framework import serializers, pagination


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    # category = CategorySerializer()
    # color = ColorSerializer

    discounted_price = serializers.SerializerMethodField()

    def get_discounted_price(self, obj):
        price = obj.price
        sale = obj.sale

        if sale is not None and sale > 0:
            discounted_price = price - (price * (sale / 100))
        else:
            discounted_price = price

        return discounted_price

    class Meta:
        model = Product
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
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


class LargeResultsSetPagination(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        pk = view.kwargs.get('pk')
        if not queryset.filter(pk=pk).exists():
            raise NotFound("Object not found with this pk")

        return super().paginate_queryset(queryset, request, view)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class EmailSerializer(Serializer):
    email = EmailField()
