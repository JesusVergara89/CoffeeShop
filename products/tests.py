from django.test import TestCase
from django.urls import reverse
from .models import Product

class ListProductsViewTests(TestCase):

    def test_should_return_200(self):
        url = reverse('list')
        response = self.client.get(url)
        #breakpoint()
        self.assertEqual(response.status_code, 200)
        
    def test_should_return_200_with_products(self):
        url = reverse('list')
        Product.objects.create(
            name="test",
            description="test description",
            price=10,       
            available=True,
            image="test.png"
        )
        response = self.client.get(url)
        #breakpoint()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['list_products'].count(), 1)