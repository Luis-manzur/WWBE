"""Calification serializers."""

# Django
from django.db.models import Avg

# Django REST Framework
from rest_framework import serializers

# Models
from califications.models import Calification

class CalificationModelSerializer(serializers.ModelSerializer):
    """Calification model serializer"""

    class Meta:
        """Meta class"""

        model = Calification
        fields = ('rating', 'message')

class CreateCalificationSerializer(serializers.ModelSerializer):
    """Create Calification serializer."""

    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    rating = serializers.IntegerField(min_value=1, max_value=5)
    message = serializers.CharField()

    class Meta:
        """Meta class."""

        model = Calification
        fields = ('rating', 'message', 'user')


    def validate(self, data):
        """Validate.

        Verify that the person who rates the accommodation is the same user making the request.
        """
        if self.context['request'].user != data['user']:
            raise serializers.ValidationError('Rate an accommodation on behalf of others is not allowed.')
            
        return data

    def create(self, data):
        """Create rating."""
        accommodation = self.context['accommodation']

        Calification.objects.create(
            accommodation=self.context['accommodation'],
            **data
        )

        accommodation_avg = round(
            Calification.objects.filter(
                rated_accommodation=accommodation
            ).aggregate(Avg('rating'))['rating__avg'],
            1
        )
        accommodation = accommodation_avg
        accommodation.save()

        return self.context['accommodation']
