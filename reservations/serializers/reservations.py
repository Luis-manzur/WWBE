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
        fields = "__all__"
        

class CreateReservationSerializer(serializers.ModelSerializer):
    """Create Reservation serializer."""

    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    departure_date = serializers.DateField()
    entrance_date = serializers.DateField()
    adults = serializers.IntegerField()
    kids = serializers.IntegerField()

    class Meta:
        """Meta class."""

        model = Reservation
        fields = ('plan', 'entrance_date', 'departure_date', 'user', 'adults', 'kids')



    def create(self, data):
        """Create reservation."""

        reservation = Reservation.objects.create(
            **data
        )
        return reservation
        

