"""Country model."""

#Django
from django.db import models

#Models
from utils.models import WWBModel

class Country(models.Model):
    """Country model.
    """
    name = models.CharField(max_length=30)

    class Admin:
        pass

    def __str__(self) -> str:
        """Return country name."""
        return str(self.name)