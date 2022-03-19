"""City model"""

#Django
from django.db import models
from utils.models import WWBModel

class City(WWBModel):
    """City model.
    """
    name = models.CharField(max_length=30)
    country = models.ForeignKey("accommodations.country", on_delete=models.DO_NOTHING, null=True)

    class Admin:
        pass

    def __str__(self) -> str:
        """Return city name"""
        return str(self.name)