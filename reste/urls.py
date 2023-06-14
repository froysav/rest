from django.urls import path

from .views import ProductAPIView, ProductUpdateDeleteAPIView, Categori, Detail, AddToShoppingCardAPIView, \
    UserShoppingCardAPIView, DeleteFromCardAPIView, LikeAPIView, ColorsAPIView, CommentListCreateView, \
    BillingRecordsView, SendMail, BlogAPIView, BlogDetailAPIView, ReviewsAPIView, BillingsRecordsView, SearchAPIView, \
    ProductDetailAPIView, CategorylistAPIView,LikelistAPIView,CardlistAPIView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('blog', BlogAPIView.as_view(), name='blog'),
    path('product-update-delete/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='products_update_delete'),
    path('category/', Categori.as_view(), name='category'),
    path('color/', ColorsAPIView.as_view(), name='color'),
    path('products/<int:pk>', ProductDetailAPIView.as_view(), name='products'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('blog/<int:pk>', BlogDetailAPIView.as_view(), name='detail'),
    path('details/<int:pk>', BlogDetailAPIView.as_view(), name='detail'),
    path('docs/', schema_view),
    path('category_list/', CategorylistAPIView.as_view(), name='category_list'),
    path('like_list/', LikelistAPIView.as_view(), name='like_list'),
    path('card_list/', CardlistAPIView.as_view(), name='card_list'),
    path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
    path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
    path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),
    path('like/', LikeAPIView.as_view(), name='like'),
    path('products/<int:pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('page/<int:pk>/', BillingRecordsView.as_view(), name='product'),
    path('pages/<int:pk>/', BillingsRecordsView.as_view(), name='billing'),
    path('send-email', SendMail.as_view(), name='send_email'),
    path('reviews', ReviewsAPIView.as_view(), name='reviews'),
    path('search/', SearchAPIView.as_view(), name='your-model-list'),
]
