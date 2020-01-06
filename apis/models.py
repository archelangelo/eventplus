import os
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import FieldError
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
import datetime

from .google_apis import Client

User = get_user_model()
SRID = 4326 # Using WGS 84

class EventManager(models.Manager):
    def create_event(self, host=None, place_id='', time=datetime.datetime.now()):
        r_json = Client.details_request(place_id=place_id)
        result = r_json['result']
        place_name = result['name']
        location = GEOSGeometry('POINT({lng} {lat})'.format(**result['geometry']['location']), srid=SRID)
        return self.create(host=host, place_id=place_id, place_name=place_name, location=location, time=time)

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    place_id = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    location = models.PointField()
    time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.place_name

def get_profile_photo_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to=get_profile_photo_path, null=True, blank=True)

# Create and save user profile when saving user data
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()