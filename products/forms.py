from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label="Product name")
    description = forms.CharField(max_length=200, label="Product description")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Product price")
    available = forms.BooleanField(initial=True, label="Product availability", required=False)
    image = forms.ImageField(label="Product image", required=False)

    def save(self):
        Product.objects.create(
           name = self.cleaned_data["name"],
           description = self.cleaned_data["description"],
           price = self.cleaned_data["price"],
           available = self.cleaned_data["available"],
           image = self.cleaned_data["image"]
        )