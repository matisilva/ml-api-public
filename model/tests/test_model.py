import unittest
import os.path
import sys
sys.path.append(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))
from ml_service import predict


class TestMLService(unittest.TestCase):

    def test_model_response(self):
        pos_sentence = 'Me gusto la pelicula'
        pos_prediction = predict(pos_sentence)
        self.assertEqual(pos_prediction[0], 'Positivo')
        self.assertAlmostEqual(pos_prediction[1], 0.7406, places=3)

        neg_sentence = 'No me gusto la pelicula'
        neg_prediction = predict(neg_sentence)
        self.assertEqual(neg_prediction[0], 'Negativo')
        self.assertAlmostEqual(neg_prediction[1], 0.255, places=3)


if __name__ == '__main__':
    unittest.main()
