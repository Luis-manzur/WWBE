"""Reservation views."""

#DjangoREST Framework
from rest_framework import viewsets, mixins

#Serializers
from reservations.serializers import ReservationModelSerializer

#Models
from reservations.models import Reservation

#Permissions
from rest_framework.permissions import IsAuthenticated
from reservations.permissions import IsReservationOwner

class ReservationViewSet( mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Reservation view set."""

    permission_classes = [IsAuthenticated, IsReservationOwner]

    serializer_class = ReservationModelSerializer
    queryset = Reservation.objects.all()
