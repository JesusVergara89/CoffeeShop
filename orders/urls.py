from django.urls import path
from .views import OrderDetailView

urlpatterns = [
   path('myorder/', OrderDetailView.as_view(), name='order_detail'),
]