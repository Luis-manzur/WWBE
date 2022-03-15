
"""Calification Model"""

#Django
from django.db import models

#Models
from accommodations.models.accommodations import Accommodation
from users.models import User

class Calification(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    message = models.CharField(max_length=255)