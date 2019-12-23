from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Event

@admin.register(Event)
class EventAdmin(OSMGeoAdmin):
    list_display = ('host', 'place_name')