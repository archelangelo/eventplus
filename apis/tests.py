from django.test import TestCase
from .google_apis import Client

class GoogleAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.place_id = 'ChIJN1t_tDeuEmsRUsoyG83frY4'
    
    def test_detail_request(self):
        response_body = self.client.details_request(self.place_id)
        self.assertIsNot(Client.GOOGLE_API_KEY, '')
        self.assertEqual(response_body['status'], 'OK')