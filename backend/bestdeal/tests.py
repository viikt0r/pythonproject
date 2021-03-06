import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from . api.brand.models import Brand
from . api.brand.serializers import BrandsSerializer
from django.contrib.auth.models import User

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


# initialize the APIClient app
client = Client()

class BrandTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.bestbuy = Brand.objects.create(id=1, name="bestbuy", link="https://m.bestbuy.ca/fr-ca", user_add=user)
        self.walmart = Brand.objects.create(id=2, name="walmart", link="https://www.walmart.ca", user_add=user)
        self.costco = Brand.objects.create(id=3, name="costco", link="https://www.costco.ca/", user_add=user)

    def test_brand_breed(self):
        costco = Brand.objects.get(name='costco')
        self.assertEqual(
            costco.test(), "costco link : https://www.costco.ca/")

