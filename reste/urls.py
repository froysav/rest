from django.urls import path

from .views import ProductAPIView, ProductUpdateDeleteAPIView, DetailAPIView, RegisterView, LoginView, Categori

urlpatterns = [
    path('products', ProductAPIView.as_view(), name='products'),
    path('details', DetailAPIView.as_view(), name='details'),
    path('product-update-delete/<int:pk>', ProductUpdateDeleteAPIView.as_view(), name='products_update_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('category/', Categori.as_view(), name='category'),
]
