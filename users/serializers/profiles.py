"""Profiles serializer"""

#Django REST Framwewrok
from rest_framework import serializers

#Models
from users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile model serializer."""

    class Meta:
        """meta class."""

        model = Profile
        fields = (
            'picture',
            'accommodations_booked',
            'comments',
        )

        read_only_fields = (
            'accommodations_booked',
            'comments',

        )
