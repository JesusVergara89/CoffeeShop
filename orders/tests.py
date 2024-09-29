from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class OrderDetailViewTests(TestCase):

    def test_not_logged_user_should_redirect_to_login(self):
        url = reverse("order_detail")
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 302)

    def test_logged_user_should_show_order_detail(self):
        url = reverse("order_detail")
        user = get_user_model().objects.create_user(username="test", password="test")
        self.client.force_login(user)
        response = self.client.get(url)
        # breakpoint()
        self.assertEqual(response.status_code, 200)
