import os
import unittest
import json

from WeConnect.app import app_factory

app = app_factory('TestingConfig')
headers = {'Content-type': 'application/json'}

class user_scenarios(unittest.TestCase):
    def setUp(self):
        self.dummyuser = app.test_client()
        self.user_data = []
    
    def test_user_registration(self):
        url = '/api/auth/registeruser'
        data = {
            'email':'adnskli@mail.com',
            'username':'u',
            'firstname': 'Frank',
            'secondname': 'yugyu',
            'password': 'adhU/da8',
            'confirmpassword':'adh/da8'
            }
        newuser = self.user_data.append(data)
        response = self.dummyuser.post(url, data=json.dumps(newuser), headers = headers)
        
        self.assertTrue(response.status_code, 201)
    
    