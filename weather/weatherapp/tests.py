from django.test import TestCase

import json 

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import City
# Create your tests here.

class CityViewSetTestCase(APITestCase):
    list_url = reverse('city-list')
    print(list_url)

    def setUp(self):
        City.objects.create(city_name='Utah')

    def test_city_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_city_detail_get(self):
        response = self.client.get(reverse('city-detail', kwargs={'slug':'utah'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(self.setUp)
    
    def test_city_detail_delete(self):
        response = self.client.delete(reverse('city-detail', kwargs={'slug':'utah'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_city_post(self):
        data = {'city_name': 'utah'}
        response = self.client.post('/api/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    