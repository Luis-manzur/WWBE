"""Image serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import Image

class ImageModelSeializer(serializers.ModelSerializer):
    """Image model serializer"""

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=Image
        fields = ("image",)