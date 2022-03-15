"""Room Model."""

#Django
from unicodedata import name
from django.db import models

#Models
from accommodations.models.plans import Plan

class Room(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(null=False)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    accommodation = models.ForeignKey('accommodations.accommodation', on_delete=models.CASCADE)