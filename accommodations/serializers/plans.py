"""Plans serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import Plan

class PlanModelSeializer(serializers.ModelSerializer):
    """Plan model serializer"""

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=Plan
        fields = "__all__"