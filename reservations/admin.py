#Django
from django.contrib import admin

#Models
from reservations.models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'entrance_date', 'plan')
    list_filter = ('created', 'plan', 'entrance_date')