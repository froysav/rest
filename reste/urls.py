from django.urls import path

from .views import ProductAPIView, ProductUpdateDeleteAPIView, Categori, Detail, AddToShoppingCardAPIView, \
    UserShoppingCardAPIView, DeleteFromCardAPIView, LikeAPIView,ColorsAPIView

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('products', ProductAPIView.as_view(), name='products'),
    path('product-update-delete/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='products_update_delete'),
    path('category/', Categori.as_view(), name='category'),
    path('color/', ColorsAPIView.as_view(), name='color'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('docs/', schema_view),
    path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
    path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
    path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),
    path('like/', LikeAPIView.as_view(), name='like'),
]