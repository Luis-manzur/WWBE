"""Plan Model."""

#Django
from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    accommodation = models.ForeignKey("accommodations.accommodation", on_delete=models.CASCADE)

    def __str__(self):
        return self.name 