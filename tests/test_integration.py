import unittest

import requests


class TestIntegration(unittest.TestCase):
    POS_SENT = 'Esta es una oracion positiva y estoy contento por eso'
    NEG_SENT = 'Tenemos problemas de inseguridad'
    NEU_SENT = 'Te invito al cine'

    def test_ok_positive(self):
        response = requests.request(
            'POST',
            'http://localhost/predict',
            params={'text': self.POS_SENT},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['prediction'], 'Positivo')

    def test_ok_negative(self):
        response = requests.request(
            'POST',
            'http://localhost/predict',
            params={'text': self.NEG_SENT},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['prediction'], 'Negativo')

    def test_ok_neutral(self):
        response = requests.request(
            'POST',
            'http://localhost/predict',
            params={'text': self.NEU_SENT},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['success'], True)
        self.assertEqual(data['prediction'], 'Neutral')

    def test_template_endpoint(self):
        response = requests.request(
            'GET',
            'http://localhost/',
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
