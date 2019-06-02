from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.test import APIClient

from . models import Brand
from . . deal.models import Deal

from . serializers import BrandsSerializer
import sys

BRANDS_URL = reverse('brand-list-nofk')


class PrivateBrandsApiTests(TestCase):
    """Test the private marques API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test',
            'test@bestdeal.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_brand_list(self):
        """Test retrieving a list of marques"""
        Brand.objects.create(user_add=self.user, name='Bestbuy', link='https://bestbuy.ca')
        Brand.objects.create(user_add=self.user, name='Amazon', link='https://amazon.ca')
        res = self.client.get(BRANDS_URL)

        brands = Brand.objects.all()

        context = {'request': RequestFactory().get('/')}
        serializer = BrandsSerializer(brands, context=context, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'], serializer.data)

    def test_brands_limited_to_user(self):
        """Test that marques for the authenticated user are returend"""
        user2 = get_user_model().objects.create_user(
            'other',
            'other@bestdeal.com',
            'testpass'
        )
        Brand.objects.create(user_add=user2, name='Bell', link='https://www.bell.ca')
        brand = Brand.objects.create(user_add=self.user, name='Videotron', link='http://videotron.com')

        res = self.client.get(BRANDS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 4)
        self.assertEqual(res.data['results'][1]['name'], brand.name)

    def test_create_brand_successful(self):
        """Test create a new marque"""
        payload = {'name': 'Costco', 'link': 'https://www.costco.ca/'}
        self.client.post(BRANDS_URL, payload)

        exists = Brand.objects.filter(
            user_add=self.user,
            name=payload['name'],
        ).exists()
        self.assertTrue(exists)

    def test_create_brand_invalid_name(self):
        """Test creating invalid marque fails"""
        payload = {'name': '', 'link': 'https://www.superc.ca/'}
        res = self.client.post(BRANDS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_brands_assigned_to_deals(self):
        """Test filtering marques by those assigned to deals"""
        brand1 = Brand.objects.create(
            user_add=self.user, name='Maxi', link='https://www.maxi.ca/'
        )
        brand2 = Brand.objects.create(
            user_add=self.user, name='Provigo', link='https://www.provigo.ca/'
        )
        deal = Deal.objects.create(
            user_add=self.user,
            title='Pomme',
            link='',
            price_after=0.15,
            country='CA',
            brand_fk=brand1
        )

        res = self.client.get(BRANDS_URL, {'assigned_only': 1})

        context = {'request': RequestFactory().get('/')}
        serializer1 = BrandsSerializer(brand1, context=context)
        serializer2 = BrandsSerializer(brand2, context=context)

        self.assertIn(serializer1.data, res.data['results'])
        #self.assertNotIn(serializer2.data, res.data['results'])

    def test_retrieve_brands_assigned_unique(self):
        """Test filtering marques by assigned returns unique items"""
        brand = Brand.objects.create(user_add=self.user, name='Tigre Geant', link='https://www.gianttiger.com/fr')
        Brand.objects.create(user_add=self.user, name='Ikea', link='https://www.ikea.com/')
        deal1 = Deal.objects.create(
            user_add=self.user,
            title='Lampe',
            link='',
            price_after=5.00,
            country='CA',
            brand_fk=brand
        )

        deal2 = Deal.objects.create(
            user_add=self.user,
            title='Rideau',
            link='',
            price_after=10.00,
            country='CA',
            brand_fk=brand
        )

        res = self.client.get(BRANDS_URL, {'assigned_only': 1})

        self.assertEqual(len(res.data), 4)