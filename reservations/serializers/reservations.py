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



    def create(self, data):
        """Create reservation."""

        Reservation.objects.create(
            **data
        )

