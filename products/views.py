from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product

class ListProductsView(TemplateView):
    template_name = "products/list_products.html"
    
    def get_context_data(self, **kwargs):
        """"
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs.get('id')
        """
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context['list_products'] = products
        return context
