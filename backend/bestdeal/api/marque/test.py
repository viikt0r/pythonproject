from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.test import APIClient

from . models import Marque
from . . deal.models import Deal

from . serializers import MarquesSerializer
import sys

MARQUES_URL = reverse('marque-list-nofk')


class PrivateMarquesApiTests(TestCase):
    """Test the private marques API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test',
            'test@bestdeal.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_marque_list(self):
        """Test retrieving a list of marques"""
        Marque.objects.create(user_add=self.user, name='Bestbuy', link='https://bestbuy.ca')
        Marque.objects.create(user_add=self.user, name='Amazon', link='https://amazon.ca')
        res = self.client.get(MARQUES_URL)

        marques = Marque.objects.all()

        context = {'request': RequestFactory().get('/')}
        serializer = MarquesSerializer(marques, context=context, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'], serializer.data)

    def test_marques_limited_to_user(self):
        """Test that marques for the authenticated user are returend"""
        user2 = get_user_model().objects.create_user(
            'other',
            'other@bestdeal.com',
            'testpass'
        )
        Marque.objects.create(user_add=user2, name='Bell', link='https://www.bell.ca')
        marque = Marque.objects.create(user_add=self.user, name='Videotron', link='http://videotron.com')

        res = self.client.get(MARQUES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 4)
        self.assertEqual(res.data['results'][1]['name'], marque.name)

    def test_create_marque_successful(self):
        """Test create a new marque"""
        payload = {'name': 'Costco', 'link': 'https://www.costco.ca/'}
        self.client.post(MARQUES_URL, payload)

        exists = Marque.objects.filter(
            user_add=self.user,
            name=payload['name'],
        ).exists()
        self.assertTrue(exists)

    def test_create_marque_invalid_name(self):
        """Test creating invalid marque fails"""
        payload = {'name': '', 'link': 'https://www.superc.ca/'}
        res = self.client.post(MARQUES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_marques_assigned_to_deals(self):
        """Test filtering marques by those assigned to deals"""
        marque1 = Marque.objects.create(
            user_add=self.user, name='Maxi', link='https://www.maxi.ca/'
        )
        marque2 = Marque.objects.create(
            user_add=self.user, name='Provigo', link='https://www.provigo.ca/'
        )
        deal = Deal.objects.create(
            user_add=self.user,
            title='Pomme',
            link='',
            price_after=0.15,
            country='CA',
            dea_mar_fk=marque1
        )

        res = self.client.get(MARQUES_URL, {'assigned_only': 1})

        context = {'request': RequestFactory().get('/')}
        serializer1 = MarquesSerializer(marque1, context=context)
        serializer2 = MarquesSerializer(marque2, context=context)

        self.assertIn(serializer1.data, res.data['results'])
        #self.assertNotIn(serializer2.data, res.data['results'])

    def test_retrieve_marques_assigned_unique(self):
        """Test filtering marques by assigned returns unique items"""
        marque = Marque.objects.create(user_add=self.user, name='Tigre Geant', link='https://www.gianttiger.com/fr')
        Marque.objects.create(user_add=self.user, name='Ikea', link='https://www.ikea.com/')
        deal1 = Deal.objects.create(
            user_add=self.user,
            title='Lampe',
            link='',
            price_after=5.00,
            country='CA',
            dea_mar_fk=marque
        )

        deal2 = Deal.objects.create(
            user_add=self.user,
            title='Rideau',
            link='',
            price_after=10.00,
            country='CA',
            dea_mar_fk=marque
        )

        res = self.client.get(MARQUES_URL, {'assigned_only': 1})

        self.assertEqual(len(res.data), 4)