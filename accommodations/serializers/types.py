"""Type serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import Type

class TypeModelSeializer(serializers.ModelSerializer):
    """Type model serializer"""

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=Type
        fields = ('name', )