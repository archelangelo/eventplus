import requests
import os
from django.core.exceptions import FieldError

class Client():

    GOOGLE_API_KEY = os.getenv('PLACES_API_KEY', '')
    GOOGLE_PLACE_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'
    GOOGLE_PLACE_NEARBY_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    GOOGLE_PLACE_TEXT_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

    @classmethod
    def details_request(cls, place_id = ''):
        params = {
            'place_id': place_id,
            'key': cls.GOOGLE_API_KEY,
            'fields': 'name,place_id,geometry',
        }
        try:
            response = requests.get(url=cls.GOOGLE_PLACE_DETAILS_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError(f'Error getting response from Google API: {err}')
        if response.status_code != 200:
            raise FieldError(f'Error getting response from Google API: Status code {response.status_code}')
        response_body = response.json()
        status = response_body.get('status', '')
        if status != 'OK':
            raise FieldError(f'Error getting response from Google API: Response status {status}')
        return response_body

    @classmethod
    def nearby_request(cls, location, radius = 1500):
        params = {
            'key': cls.GOOGLE_API_KEY,
            'location': location,
            'radius': radius,
        }
        try:
            response = requests.get(url=cls.GOOGLE_PLACE_NEARBY_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError(f'Error getting response from Google API: {err}')
        if response.status_code != 200:
            raise FieldError(f'Error getting response from Google API: Status code {response.status_code}')
        response_body = response.json()
        status = response_body.get('status', '')
        if status != 'OK':
            raise FieldError(f'Error getting response from Google API: Response status {status}')
        return response_body

    @classmethod
    def textsearch_request(cls, query, location=None, radius=None):
        params = {
            'key': cls.GOOGLE_API_KEY,
            'query': query,
        }
        if location:
            params['location'] = location
        if radius:
            params['radius'] = radius
        try:
            response = requests.get(url=cls.GOOGLE_PLACE_TEXT_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError(f'Error getting response from Google API: {err}')
        if response.status_code != 200:
            raise FieldError(f'Error getting response from Google API: Status code {response.status_code}')
        response_body = response.json()
        status = response_body.get('status', '')
        if status != 'OK':
            raise FieldError(f'Error getting response from Google API: Response status {status}')
        return response_body