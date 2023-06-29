from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class MyAPITestCase(APITestCase):
    def setUp(self):
        # Set up any required data for your tests
        ...

    def test_my_endpoint(self):
        # Define the URL for your API endpoint
        url = reverse("my-endpoint")

        # Define the request data
        data = {
            "key1": "value1",
            "key2": "value2",
        }

        # Make a POST request to the endpoint
        response = self.client.post(url, data)

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert the response data or any other expectations
        ...

        # You can also test GET, PUT, PATCH, DELETE requests similarly
