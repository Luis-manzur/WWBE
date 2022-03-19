"""Room serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import Room

class RoomModelSeializer(serializers.ModelSerializer):
    """Room model serializer"""

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=Room
        fields = ("name", "description", "image", "beds", "capacity")