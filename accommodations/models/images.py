"""Accommodation Images."""

#Django
from django.db import models

#Utilities
from utils.models import WWBModel


class Image(WWBModel):
    """Accommodation image model"""
    image = models.ImageField()
    accommodations = models.ForeignKey('accommodations.accommodation', related_name='images', on_delete=models.CASCADE)