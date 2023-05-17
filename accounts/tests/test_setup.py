from rest_framework.test import APITestCase
from django.urls import reverse


class SetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse("signup")
        return super().setUp()

        user_data = {
            "first_name": "John",
            "last_name": "RUKUNDO",
            "email": "testemail.ecommerce@api.com",
            "phone_number": "0789893412",
        }

    def tearDown(self):
        return super().tearDown()
