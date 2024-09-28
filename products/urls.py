from django.urls import path
from .views import ListProductsView, ProductFormView

urlpatterns = [
    path('', ListProductsView.as_view(), name='list'),
    path('add/', ProductFormView.as_view(), name='add'),
]