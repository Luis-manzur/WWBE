"""Reservations serializers."""

# Django
from django.utils import timezone


# Django REST Framework
from rest_framework import serializers

# Models
from reservations.models import Reservation

#Serializers
from accommodations.serializers import PlanModelSeializer

class ReservationModelSerializer(serializers.ModelSerializer):
    """Reservation model serializer"""
    
    plan = PlanModelSeializer(read_only=True)

    class Meta:
        """Meta class"""

        model = Reservation
        fields = ('plan', 'entrance_date', 'departure_date')
        

class CreateReservationSerializer(serializers.ModelSerializer):
    """Create Reservation serializer."""

    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    departure_date = serializers.DateField()
    entrance_date = serializers.DateField()

    class Meta:
        """Meta class."""

        model = Reservation
        fields = ('plan', 'entrance_date', 'departure_date', 'user')


    def validate_entrance_date(self, data):
        """Validate.

        Verify that the dates introduced are valid.
        """

        min_date = timezone.now()
        if data['entrance_date'] < min_date:
            raise serializers.ValidationError('Entrance date must be from tomorrow onwards')

        return data
    
    def validate_entrance_date(self, data):
        """Validate.

        Verify that the dates introduced are valid.
        """

        if data['entrance_date'] > data['departure_date']:
            raise serializers.ValidationError('Entrance date must be from tomorrow onwards')

        return data


    def create(self, data):
        """Create reservation."""

        Reservation.objects.create(
            **data
        )

