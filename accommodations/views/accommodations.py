"""Accommodations views."""

#DjangoREST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from accommodations.models.cities import City

#Serializers
from accommodations.serializers import AccommodationModelSeializer
from califications.serializers import CreateCalificationSerializer, CalificationModelSerializer
from reservations.serializers import ReservationModelSerializer, CreateReservationSerializer

#Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

#Models
from accommodations.models import Accommodation, accommodations

#Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsAccountOwner

class AccommodationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """Accommodation view set."""

    lookup_field = 'slug_name'
    serializer_class = AccommodationModelSeializer

    #Filters
    filter_backends = [SearchFilter]
    search_fields = ['city']
    ordering = ('-rating')

    def get_permissions(self):
        """Addign permissiond based on actions"""

        if self.action in ['rate', 'reserve']:
            permissions = [IsAuthenticated]
        else:
            permissions = [AllowAny,]

        return [permission() for permission in permissions]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Accommodation.objects.all()
        city = self.request.query_params.get('city')
        city_id = City.objects.filter(name=city).first()
        if city_id:
            queryset = Accommodation.objects.filter(city=city_id.id)
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