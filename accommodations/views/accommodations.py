"""Accommodations views."""

#DjangoREST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

#Serializers
from accommodations.serializers import AccommodationModelSeializer
from califications.serializers import CreateCalificationSerializer, CalificationModelSerializer
from reservations.serializers import ReservationModelSerializer, CreateReservationSerializer

#Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

#Models
from accommodations.models import Accommodation, accommodations

class AccommodationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Accommodation view set."""

    lookup_field = 'slug_name'
    serializer_class = AccommodationModelSeializer

    #Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('slug_name', 'name', 'country', 'city')
    ordering = ('-rating')

    def get_permissions(self):
        """Assign permissions based on actions"""
        permissions = [IsAuthenticated]
        return [permission()for permission in permissions]

    def get_queryset(self):
        """Restrict list to public only"""

        queryset = Accommodation.objects.all()
        if self.action == 'list':
            return queryset.all()
        return queryset

    @action(detail=True, methods=['POST'])
    def rate(self, request, *args, **kwargs):
        """Rate Accommodation."""
        accommodation = self.get_object()
        serializer_class = CreateCalificationSerializer
        context = self.get_serializer_context()
        context['accommodation'] = accommodation
        serializer = serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        calification = serializer.save()
        data = CalificationModelSerializer(calification).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['POST'])
    def reserve(self, request, *args, **kwargs):
        """Reserve accommodation."""
        serializer_class = CreateReservationSerializer
        context = self.get_serializer_context()
        serializer = serializer_class(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        reservation = serializer.save()
        data = ReservationModelSerializer(reservation).data
        return Response(data, status=status.HTTP_201_CREATED)