"""Accommodation model."""

#Django
from django.db import models

#Utilities
from utils.models import WWBModel

class Accommodation(WWBModel):
    """Accommodation model."""

    #About
    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)
    type = models.ForeignKey("accommodations.type", on_delete=models.DO_NOTHING, null=True)
    principal_image = models.ImageField(null=False)

    #Address
    city = models.ForeignKey("Accommodations.citiy", on_delete=models.DO_NOTHING, null=True)
    country = models.ForeignKey("accommodations.country", on_delete=models.DO_NOTHING, null=True)
    address = models.CharField(max_length=60)

    #Stats
    rating = rating = models.FloatField(default=5)

    def __str__(self):
        return self.name



