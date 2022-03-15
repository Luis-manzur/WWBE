#Django
from pyexpat import model
from django.contrib import admin

#models
from accommodations.models import Accommodation, Plan, Service, ServiceAccommodation, Image, Type, Room


class ServiceInline(admin.TabularInline):
    model = ServiceAccommodation
    fk = "service"

class ImageInline(admin.TabularInline):
    model = Image
    fk = "accommodation" 
class RoomInline(admin.TabularInline):
    model = Room
    fk = "accommodation"
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    inlines = [ServiceInline, ImageInline]
    list_display = ('pk', 'name', 'rating', 'accommodation_type', 'owner')
    list_filter = ('rating', 'accommodation_type', 'city')
    search_fields = ('name', 'accommodation_type', 'city', 'owner')

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)
