"""Room Model."""

#Django
from unicodedata import name
from django.db import models

#Models
from accommodations.models.plans import Plan
from utils.models import WWBModel

#Cloudinary
from cloudinary.models import CloudinaryField

class Room(WWBModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = CloudinaryField('image')
    beds = models.IntegerField()
    capacity = models.IntegerField()
    accommodation = models.ForeignKey('accommodations.accommodation', related_name='rooms', on_delete=models.CASCADE)