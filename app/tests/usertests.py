import os
import unittest
import json

from app.api.users import app

class usercase(unittest.TestCase):
    def setUp(self):
        self.postman = app.test_client()
    
    def test_user_registration(self):
        response = self.postman.get('/registeruser')
        self.assertEqual(json.loads(response.data)['hello'], 'world')
        