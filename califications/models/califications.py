
"""Calification Model"""

#Django
from django.db import models

#Models
from accommodations.models.accommodations import Accommodation
from users.models import User
from utils.models import WWBModel

class Calification(WWBModel):
    accommodation = models.ForeignKey(Accommodation, related_name='califications', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    message = models.CharField(max_length=255)