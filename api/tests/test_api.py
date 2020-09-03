from unittest import TestCase
from unittest.mock import patch
import json
import os.path
import sys
sys.path.append(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))
from app import app


class TestIntegration(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.sent = 'Esta es una oracion'

    def test_bad_parameters(self):
        response = self.client.post(
            '/predict',
            data=json.dumps({'text': self.sent}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['success'], False)

    @patch('views.model_predict')
    def test_ok_positive(self, mock):
        mock.return_value = ("positiva", 0.9)
        response = self.client.post(
            '/predict',
            query_string={'text': self.sent},
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['success'], True)

    @patch('views.model_predict')
    def test_ok_negative(self, mock):
        mock.return_value = ("negativa", 0.2)
        response = self.client.post(
            '/predict',
            query_string={'text': self.sent},
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['success'], True)


class TestEnpointsAvailability(TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)

    def test_feedback(self):
        response = self.client.get('/feedback')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/feedback')
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        response = self.client.get('/predict')
        # Method not allowed
        self.assertEqual(response.status_code, 405)
        response = self.client.post('/predict')
        # Bad args
        self.assertEqual(response.status_code, 400)
