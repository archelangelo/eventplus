from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import FieldError
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
import datetime

from .google_apis import Client

User = get_user_model()
SRID = 4326 # Using WGS 84

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    location = models.PointField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place_name

    @classmethod
    def create(cls, host=None, place_id='', time=datetime.datetime.now()):
        client = Client()
        r_json = client.details_request()
        result = r_json['result']
        place_name = result['name']
        location = GEOSGeometry('POINT({lng} {lat})'.format(**result['geometry']['location']), srid=SRID)
        return cls(host=host, place_id=place_id, place_name=place_name, location=location, time=time)
