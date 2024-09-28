from django.urls import path
from .views import ListProductsView, ProductFormView, ProductListAPI

urlpatterns = [
    path('', ListProductsView.as_view(), name='list'),
    path('add/', ProductFormView.as_view(), name='add'),
    path('api/products/', ProductListAPI.as_view(), name='api_products'),
]