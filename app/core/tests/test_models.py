from re import S
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@london', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        Test Create User
        """
        email = "test@gmail.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
 
    def test_new_user_email_normalized(self):
        """
        Test the email for a new user us normalized
        """
        email='test@Gmail.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error  
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
            email="",
            password="123456"
        )

    def test_create_new_super_user(self):
        """
        Test creating a new superuser
        """
        user = get_user_model().objects.create_superuser(
            email="test@test.com",
            password="123456"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """
        Test tag representation
        """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
