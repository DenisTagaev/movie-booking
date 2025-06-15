"""
Unit tests for the CustomUser model.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

CustomUser = get_user_model()
class CustomUserModelTest(TestCase):
    """
    Test cases for custom user model and data from the frontend
    """
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'user@example.com'
        password = 'securepassword123'
        user = CustomUser.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_email_is_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'Test@EXAMPLE.com'
        user = CustomUser.objects.create_user(email=email, password='pass1234')
        self.assertEqual(user.email, 'Test@example.com')

    def test_create_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='', password='pass1234')

    def test_create_superuser_successful(self):
        """Test creating a new superuser"""
        email = 'admin@example.com'
        password = 'adminpass'
        superuser = CustomUser.objects.create_superuser(email=email, password=password)

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_duplicate_email_raises_error(self):
        """Test that creating two users with the same email raises an IntegrityError"""
        email = 'duplicate@example.com'
        CustomUser.objects.create_user(email=email, password='pass1')
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(email=email, password='pass2')

    def test_create_user_without_password_raises_error(self):
        """Test that creating a user without a password raises a ValueError"""
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(email='user@example.com', password='')