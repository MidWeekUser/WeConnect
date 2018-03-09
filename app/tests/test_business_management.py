import os
import unittest
import json

from WeConnect.app import app_factory

app = app_factory('TestingConfig')

class business_scenarios(unittest.TestCase):
    def setUp(self):
        self.postman = app.test_client()
        #self.header = {'Content-type': 'application/json'}
    
    def test_business_registration(self):
        response = self.postman.post('/api/businesses', data=json.dumps({
            'businessname':'',
            'category': 'Travel',
            'location': 'Nairobi'
            }))
        self.assertTrue(response.status_code == 201)

    def test_business_reviews(self):
        response = self.postman.post('/api/businesses/reviews', data=json.dumps({
            'businessreview':'This',
            }))
        self.assertFalse(response.status_code == 201)


        