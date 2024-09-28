from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import Product
from django.views import generic
from .forms import ProductForm

class ListProductsView(generic.ListView):
    model = Product
    template_name = "products/list_products.html"
    context_object_name = 'list_products'

    
class ProductFormView(generic.FormView):
    template_name = "products/add_products.html"

    form_class = ProductForm
    success_url = reverse_lazy('add')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

