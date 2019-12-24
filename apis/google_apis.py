import requests
import os

class Client():

    GOOGLE_API_KEY = os.environ['PLACES_API_KEY']
    GOOGLE_PLACE_DETAILS_URL = 'https://maps.googleapis.com/maps/api/place/details/json'

    def details_request(self, place_id = ''):
        params = {
            'place_id': place_id,
            'key': GOOGLE_API_KEY,
            'fields': 'name,place_id,geometry',
        }
        try:
            r = requests.get(url=GOOGLE_PLACE_DETAILS_URL, params=params)
        except requests.exceptions.RequestException as err:
            print(err)
            raise FieldError('Error getting response from Google API: {}'.format(err))
        if r.status_code != 200:
            raise FieldError('Error getting response from Google API: Status code {}'.format(r.status_code))
        return r.json()