from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.test import APIClient

from . models import Tag 
from . . deal.models import Deal
from . . marque.models import Marque

from . serializers import TagSerializer


TAGS_URL = reverse('tag-list-nofk')


class PrivateTagsApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test',
            'test@bestdeal.com',
            'password123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(user_add=self.user, name='High-Tech')
        Tag.objects.create(user_add=self.user, name='Consoles & jeux vidéo')

        res = self.client.get(TAGS_URL)
        tags = Tag.objects.all()

        context = {'request': RequestFactory().get('/')}
        serializer = TagSerializer(tags, context=context, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'], serializer.data)

    def test_tags_limited_to_user(self):
        """Test that tags returned are for the authenticated user"""
        user2 = get_user_model().objects.create_user(
            'other',
            'other@bestdeal.com',
            'testpass'
        )
        Tag.objects.create(user_add=user2, name='Courses')
        tag = Tag.objects.create(user_add=self.user, name='Epicerie')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 4)
        self.assertEqual(res.data['results'][1]['name'], tag.name)

    def test_create_tag_successful(self):
        """Test creating a new tag"""
        payload = {'name': 'Test tag'}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(
            user_add=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(TAGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_tags_assigned_to_deals(self):
        """Test filtering tags by those assigned to deals"""
        tag1 = Tag.objects.create(user_add=self.user, name='Caméras')
        tag2 = Tag.objects.create(user_add=self.user, name='Casques')
        marque = Marque.objects.create(
            user_add=self.user, name='Maxi', link='https://www.maxi.ca/'
        )
        deal = Deal.objects.create(
            user_add=self.user,
            title='Gopro',
            link='',
            price_after=300.00,
            country='CA',
            dea_mar_fk=marque
        )
        deal.tag_set.add(tag1)

        res = self.client.get(TAGS_URL, {'assigned_only': 1})

        context = {'request': RequestFactory().get('/')}
        serializer1 = TagSerializer(tag1, context=context)
        serializer2 = TagSerializer(tag2, context=context)

        self.assertIn(serializer1.data, res.data['results'])
        #self.assertNotIn(serializer2.data, res.data)

    def test_retrieve_tags_assigned_unique(self):
        """Test filtering tags by assigned returns unique items"""
        tag = Tag.objects.create(user_add=self.user, name='Audio')
        Tag.objects.create(user_add=self.user, name='Console')
        marque1 = Marque.objects.create(
            user_add=self.user, name='Bestbuy', link='https://bestbuy.ca'
        )
        marque2 = Marque.objects.create(
            user_add=self.user, name='Amazon', link='https://amazon.ca'
        )
        deal1 = Deal.objects.create(
            user_add=self.user,
            title='Beat',
            link='',
            price_after=150.00,
            country='CA',
            dea_mar_fk=marque1
        )
        deal1.tag_set.add(tag)
        deal2 = Deal.objects.create(
            user_add=self.user,
            title='Xbox',
            link='',
            price_after=233.15,
            country='CA',
            dea_mar_fk=marque2
        )
        deal2.tag_set.add(tag)

        res = self.client.get(TAGS_URL, {'assigned_only': 1})

        self.assertEqual(len(res.data), 4)