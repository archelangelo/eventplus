from django.test import TestCase
from .google_apis import Client

class GoogleAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'
    
    def test_details_request(self):
        self.assertIsNot(Client.GOOGLE_API_KEY, '')
        response_body = self.client.details_request(self.place_id)
        self.assertEqual(response_body['status'], 'OK')