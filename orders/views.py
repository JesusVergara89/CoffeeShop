from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderForm


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user, is_active=True).first()


class AddProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/add_product.html"
    form_class = OrderForm
    success_url = reverse_lazy("order_detail")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
