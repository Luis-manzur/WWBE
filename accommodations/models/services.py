"""Service Model."""

#Django
from django.db import models

#Models
from accommodations.models.accommodations import Accommodation

class Service(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class ServiceAccommodation(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)