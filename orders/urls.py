from django.urls import path
from .views import OrderDetailView, AddProductView

urlpatterns = [
    path("myorder/", OrderDetailView.as_view(), name="order_detail"),
    path("addproduct/", AddProductView.as_view(), name="add_product"),
]
