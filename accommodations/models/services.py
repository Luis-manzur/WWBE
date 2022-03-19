"""Service Model."""

#Django
from django.db import models

#Models
from utils.models import WWBModel

class Service(WWBModel):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
