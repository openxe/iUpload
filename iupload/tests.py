# -*- coding: utf-8 -*-
import json
from django.test import TestCase, Client

class UploadApiTests(TestCase):

    def test_is_json(self):
        response = self.client.post('/upload', data={})
        self.assertRaises(json.loads(response.content))

    def test_empty_response(self):
        response = self.client.post('/upload', data={})
        data = json.loads(response.content)

        self.assertTrue('response' in data)
        self.assertTrue('errors' in data['response'])
        self.assertTrue('file' in data['response']['errors'])
