"""Accommodation Urls."""

#Django
from django.urls import path, include

#Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from accommodations.views import accommodations as accommodation_views


router = DefaultRouter()
router.register(r'accommodations', accommodation_views.AccommodationViewSet, basename='accommodation')

urlpatterns = [
    path('', include(router.urls))
]
