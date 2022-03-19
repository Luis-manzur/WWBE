"""accommodations serializers."""

#Django REST Framework
from rest_framework import serializers

#Model
from accommodations.models import Accommodation, Image

#Serializers
from accommodations.serializers.cities import CityModelSeializer
from accommodations.serializers.images import ImageModelSeializer
from accommodations.serializers.plans import PlanModelSeializer
from accommodations.serializers.rooms import RoomModelSeializer
from accommodations.serializers.services import ServiceModelSeializer
from accommodations.serializers.types import TypeModelSeializer
from califications.serializers import CalificationModelSerializer

class AccommodationModelSeializer(serializers.ModelSerializer):
    """Accommodation model serializer."""

    images = ImageModelSeializer(read_only=True, many=True)
    city = CityModelSeializer(read_only=True)
    type = TypeModelSeializer(read_only=True)
    plans = PlanModelSeializer(read_only=True, many=True)
    califications = CalificationModelSerializer(read_only=True, many=True)
    services = ServiceModelSeializer(read_only=True, many=True)
    rooms = RoomModelSeializer(read_only=True, many=True)

    class Meta:
        """Meta class.
        define the db model its going to use and wich fields are going to be displayed"""
        model=Accommodation
        fields = ('slug_name', 'name', 'principal_image', 'address', 'city', 'images', 'services', 'type', 'plans', 'califications', 'rooms')
        depth  = 1