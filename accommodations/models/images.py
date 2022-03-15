"""Accommodation Images."""

#Django
from django.db import models

#Utilities
from utils.models import WWBModel


class Image(models.Model):
    """Accommodation image model"""
    image = models.ImageField()
    accommodations = models.ForeignKey('accommodations.accommodation', on_delete=models.CASCADE, null=True)