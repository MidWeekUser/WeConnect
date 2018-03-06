import os
import unittest
import json

from app.api.helloworld import app

class helloworldtestcase(unittest.TestCase):
    def setUp(self):
        self.postman = app.test_client()
    
    def test_return_helloworld(self):
        response = self.postman.get('/hello')
        self.assertEqual(json.loads(response.data)['hello'], 'world')