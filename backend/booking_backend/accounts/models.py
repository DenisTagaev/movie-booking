"""
Custom user model for the Movie Booking App.

This module defines a custom user model that replaces Django's default `username`
with a unique `email` field as the primary identifier. It allows for future extensibility
to include additional user information such as full name, age, and phone number.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

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

    def __str__(self):
        return self.email
