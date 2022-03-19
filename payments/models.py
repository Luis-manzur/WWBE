"""Payment Model"""

#Django
from django.db import models

#Models
from reservations.models import Reservation
from utils.models import WWBModel

class Payment(WWBModel):
    PAYMENT_METHODS_CHOICES = [("DC",'Debit Card'), ('CC','Credit Card')]
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)