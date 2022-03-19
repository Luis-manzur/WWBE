"""Profile model."""

#Django
from django.db import models

#Utilities
from utils.models import WWBModel

#Cloudinary
from cloudinary.models import CloudinaryField

class Profile(WWBModel):
    """Profile model,

    Aprofile holds user's public data like biography, picture, and statistics.
    """

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE
    )

    picture = CloudinaryField('image', blank=True)

    #Stats
    accommodations_booked = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        """Returen user's str reptresentation"""
        return str(self.user)


