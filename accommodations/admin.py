#Django
from pyexpat import model
from django.contrib import admin

#models
from accommodations.models import Accommodation, Plan, Service, Image, Type, Room
from accommodations.models.cities import City
from accommodations.models.countries import Country

class PlanInline(admin.TabularInline):
    model=Plan
    fk="accommodation"

class RoomInline(admin.TabularInline):
    model=Room
    fk='accommodation'

class ImageInline(admin.TabularInline):
    model = Image
    fk = "accommodation" 
class RoomInline(admin.TabularInline):
    model = Room
    fk = "accommodation"
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    inlines = [ImageInline, PlanInline, RoomInline]
    list_display = ('pk', 'name', 'rating', 'type')
    list_filter = ('rating', 'type', 'city')
    search_fields = ('name', 'type', 'city')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_editable = ('name',)

@admin.register(City)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_filter = ('country',)

@admin.register(Country)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

