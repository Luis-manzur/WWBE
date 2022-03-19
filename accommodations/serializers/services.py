"""Service serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import Service

class ServiceModelSeializer(serializers.ModelSerializer):
    """Sevice model serializer"""

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=Service
        fields = ("name",)