"""Accommodations type model"""

#Django
from django.db import models

class Type(models.Model):
    """Accommodation type model.
    """
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        """Return type string representation."""
        return str(self.name)