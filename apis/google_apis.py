import requests
import os
from django.core.exceptions import FieldError

class Client():

    GOOGLE_API_KEY = os.getenv('PLACES_API_KEY', '')
    GOOGLE_PLACE_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'
    GOOGLE_PLACE_NEARBY_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    GOOGLE_PLACE_TEXT_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

    def details_request(self, place_id = ''):
        params = {
            'place_id': place_id,
            'key': Client.GOOGLE_API_KEY,
            'fields': 'name,place_id,geometry',
        }
        try:
            r = requests.get(url=Client.GOOGLE_PLACE_DETAILS_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError('Error getting response from Google API: {}'.format(err))
        if r.status_code != 200:
            raise FieldError('Error getting response from Google API: Status code {}'.format(r.status_code))
        return r.json()

    def nearby_request(self):
        params = {
            'key': Client.GOOGLE_API_KEY,
            'fields': 'name,place_id,geometry',
        }
        try:
            r = requests.get(url=Client.GOOGLE_PLACE_NEARBY_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError('Error getting response from Google API: {}'.format(err))
        if r.status_code != 200:
            raise FieldError('Error getting response from Google API: Status code {}'.format(r.status_code))
        return r.json()

    def textsearch_request(self):
        params = {
            'key': Client.GOOGLE_API_KEY,
            'fields': 'name,place_id,geometry',
        }
        try:
            r = requests.get(url=Client.GOOGLE_PLACE_TEXT_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError('Error getting response from Google API: {}'.format(err))
        if r.status_code != 200:
            raise FieldError('Error getting response from Google API: Status code {}'.format(r.status_code))
        return r.json()