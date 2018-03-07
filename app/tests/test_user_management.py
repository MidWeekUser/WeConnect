import os
import unittest
import json

from WeConnect.app import app_factory

app = app_factory('TestingConfig')

class user_scenarios(unittest.TestCase):
    def setUp(self):
        self.postman = app.test_client()
        self.header = {'Content-type': 'application/json'}
    
    def test_user_registration(self):
        response = self.postman.post('/api/auth/registeruser', data=json.dumps({
            'email':'adnskli',
            'username':'Dhodia',
            'firstname': 'Frank',
            'secondname': 'Wams',
            'password': 'adhuda',
            'confirmpassword':'adhuda'
            }),headers=self.header)
        self.assertFalse(response.status_code == 302)

        