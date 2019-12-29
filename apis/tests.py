from django.test import TestCase
from django.contrib.auth.models import User
from .google_apis import Client
from .models import Event

class GoogleAPITestCase(TestCase):
    def setUp(self):
        self.place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'
        self.location = '-33.8670522,151.1957362'
        self.radius = 1500
        self.query = 'georgia tech'
    
    def test_details_request(self):
        self.assertIsNot(Client.GOOGLE_API_KEY, '')
        response_body = Client.details_request(self.place_id)
        self.assertEqual(response_body['status'], 'OK')

    def test_nearby_request(self):
        self.assertIsNot(Client.GOOGLE_API_KEY, '')
        response_body = Client.nearby_request(self.location, self.radius)
        self.assertEqual(response_body['status'], 'OK')

    def test_textsearch_request(self):
        self.assertIsNot(Client.GOOGLE_API_KEY, '')
        response_body = Client.textsearch_request(self.query, self.location, self.radius)
        self.assertEqual(response_body['status'], 'OK')

class EventModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='a@mm.com', password='top_secret')
        self.place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'
        self.place_name = 'Google Australia'

    def test_event_creation(self):
        Event.objects.create_event(host=self.user, place_id=self.place_id)
        self.assertEqual(Event.objects.get().place_name, self.place_name)