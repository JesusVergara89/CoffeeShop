from django.forms import ModelForm
from .models import OrderProduct


class OrderForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ["product"]
