"""User model."""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from utils.models import WWBModel

class User(WWBModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        max_length=17,
        blank=True,
        validators=[phone_regex]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_active = models.BooleanField(
        'Active status',
        default=True,
        help_text=(
            'Hellp easily distinguish users and perform queries.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user hacve verified the email address.'
    )

    def __str__(self) -> str:
        """Return username"""
        return self.username

    def get_short_name(self) -> str:
        """Return username"""
        return self.username
