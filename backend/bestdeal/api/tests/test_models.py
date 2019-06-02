from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from . . brand import models
from . . tag import models
from . . deal import models
from django.contrib.auth.models import User


class ModelTests(TestCase):

    #user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
    #self.user = User.objects.get(username='foo')

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        username = 'dbest'
        email = 'test@bestdeal.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        username = "test2"
        email = 'test@bestdeal.COM'
        user = get_user_model().objects.create_user(username, email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'name4',
            'test@bestdeal.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        self.u1 = User.objects.create(username='user1')
        tag = models.Tag.objects.create(
            user_add=self.u1,
            name='Telephone'
        )

        self.assertEqual(str(tag), tag.name)

    def test_brand_str(self):
        """Test the marque string respresentation"""
        self.u2 = User.objects.create(username='user2')
        brand = models.Brand.objects.create(
            user_add=self.u2,
            name='amazon',
            link='https://amazon.ca'
        )

        self.assertEqual(str(brand), brand.name)

    def test_deal_str(self):
        """Test the deal string representation"""
        self.u3 = User.objects.create(username='user3')
        brand = models.Brand.objects.create(
            user_add=self.u3,
            name='amazon',
            link='https://amazon.ca'
        )
        deal = models.Deal.objects.create(
            user_add=self.u3,
            title='TV',
            link='',
            price_after=5.00,
            country='CA',
            brand_fk=brand
        )

        self.assertEqual(str(deal), deal.title)
