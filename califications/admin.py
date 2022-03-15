#Django
from django.contrib import admin

#Models
from califications.models import Calification


@admin.register(Calification)
class CalificationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'accommodation', 'rating')
    list_filter = ('accommodation', 'rating')
    search_fields = ('user',)