"""Plan Model."""

#Django
from django.db import models

#Models
from utils.models import WWBModel

class Plan(WWBModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    adult_price = models.FloatField()
    children_price = models.FloatField()
    accommodation = models.ForeignKey("accommodations.accommodation", related_name='plans', on_delete=models.CASCADE)

    def __str__(self):
        return self.name 