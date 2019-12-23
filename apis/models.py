from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
import requests
import os

User = get_user_model()
GOOGLE_API_KEY = os.environ['PLACES_API_KEY']
GOOGLE_PLACE_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'
SRID = 4326 # Using WGS 84

class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    place_id = models.CharField(max_length=100)
    place_name = models.CharField(max_length=100)
    location = models.PointField()
    time = models.DateTimeField()

    def __str__(self):
        return self.place_name

    def clean(self):
        params = {
            'place_id': self.place_id,
            'key': GOOGLE_API_KEY,
            'fields': 'name,place_id,geometry',
        }
        try:
            r = requests.get(url=GOOGLE_PLACE_DETAILS_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise ValidationError('Error getting response from Google API: {}'.format(err))
        if r.status_code != 200:
            raise ValidationError('Error getting response from Google API: Status code {}'.format(r.status_code))
        result = r.json()['result']
        self.place_name = result['name']
        self.location = GEOSGeometry('POINT({lng} {lat})'.format(**result['geometry']['location']), srid=SRID)
