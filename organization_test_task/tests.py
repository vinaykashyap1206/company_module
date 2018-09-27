from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.get('/companies/', format="json")

    def test_api_to_get_company_details(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
