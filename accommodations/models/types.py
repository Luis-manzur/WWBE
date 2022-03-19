"""Accommodations type model"""

#Django
from django.db import models

#Model
from utils.models import WWBModel

class Type(WWBModel):
    """Accommodation type model.
    """
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        """Return type string representation."""
        return str(self.name)