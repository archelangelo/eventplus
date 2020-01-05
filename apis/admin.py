from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Event, UserProfile

@admin.register(Event)
class EventAdmin(OSMGeoAdmin):
    list_display = ('host', 'place_name')

admin.site.register(UserProfile)