"""
Custom user model and manager for the Movie Booking App.

This module defines a custom user model and custom helper manager that replace Django's default
with a unique `email` field as the primary identifier. It allows for future extensibility
to include additional user information such as full name, age, and phone number.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.

    Provides methods to create regular users and superusers using email instead of username.
    Ensures that required fields like email and password are properly validated and normalized.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and returns a new user with the given email and password.

        Raises:
            ValueError: If the email or password is not provided.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            **extra_fields: Additional fields to include on the user model.

        Returns:
            CustomUser: The created user instance.
        """

        if not email:
            raise ValueError('The Email must be set')
        if not password:
            raise ValueError('The Password must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a new superuser with the given email and password.

        Raises:
            ValueError: If the email or password is not provided.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            **extra_fields: Additional fields to include on the user model.

        Returns:
            CustomUser: The created user instance.
        """

        if not email:
            raise ValueError('The Email must be set')
        if not password:
            raise ValueError('Superusers must have a password')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model that uses email instead of username for authentication.

    This model inherits from Django's AbstractUser but disables the default `username`
    field in favor of a unique `email`. It is designed to support user accounts in
    the Movie Booking App, with flexibility to add additional profile fields in the future.

    Attributes:
        email (EmailField): The user's email address

    Future Fields (commented out):
        full_name (CharField): The full name of the user.
        age (PositiveIntegerField): The age of the user.
        phone (CharField): The user's phone number.

    Class Attributes:
        USERNAME_FIELD (str): Field used for authentication (set to 'email').
        

    Returns:
        str: The user's email address.
    """

    username = None
    email = models.EmailField(unique=True)

    # Future fields
    # full_name = models.CharField(max_length=100, blank=True)
    # age = models.PositiveIntegerField(null=True, blank=True)
    # phone = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
