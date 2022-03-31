"""Reservation model"""

#Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#Models
from accommodations.models import Plan
from users.models import User
from utils.models import WWBModel

class Reservation(WWBModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    plan = models.ForeignKey(Plan, on_delete=models.DO_NOTHING)
    adults = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], null=True)
    kids = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)], null=True)
    entrance_date = models.DateField()
    departure_date = models.DateField()