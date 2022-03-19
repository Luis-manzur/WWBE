"""Accommodation model."""

#Django
from django.db import models

#Utilities
from utils.models import WWBModel

#Cloudinary
from cloudinary.models import CloudinaryField

class Accommodation(WWBModel):
    """Accommodation model."""

    #About
    name = models.CharField('Accommodation name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)
    type = models.ForeignKey("accommodations.type", on_delete=models.DO_NOTHING, null=True)
    principal_image = CloudinaryField('image')
    services = models.ManyToManyField("accommodations.service")
    #Address
    city = models.ForeignKey("accommodations.city", on_delete=models.DO_NOTHING, null=True)
    country = models.ForeignKey("accommodations.country", on_delete=models.DO_NOTHING, null=True)
    address = models.CharField(max_length=60)

    #Stats
    rating = rating = models.FloatField(default=5)

    def __str__(self):
        return self.name



