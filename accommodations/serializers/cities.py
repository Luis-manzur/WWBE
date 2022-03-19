"""Cities serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import City

#Serializers
from accommodations.serializers.countries import CountryModelSeializer

class CityModelSeializer(serializers.ModelSerializer):
    """City model serializer"""

    country = CountryModelSeializer(read_only=True)

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=City
        fields = ('name', "country")