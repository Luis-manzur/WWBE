"""Reservation model"""

#Django
from django.db import models

#Models
from accommodations.models import Plan
from users.models import User
from utils.models import WWBModel

class Reservation(WWBModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING )
    plan = models.ForeignKey(Plan, on_delete=models.DO_NOTHING)
    entrance_date = models.DateTimeField()
    departure_date = models.DateTimeField()