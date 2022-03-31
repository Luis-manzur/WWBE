"""Reservations Urls."""

#Django
from django.urls import path, include

#Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from reservations.views import ReservationViewSet


router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='reservations')

urlpatterns = [
    path('', include(router.urls))
]