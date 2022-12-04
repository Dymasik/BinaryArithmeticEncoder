from unittest import TestCase

from src.encoder.binary_arithmetic_encoder import BinaryArithmeticEncoder


class TestBinaryArithmeticEncoder(TestCase):
    def setUp(self) -> None:
        self.encoder = BinaryArithmeticEncoder({
            'A': 0.4,
            'B': 0.3,
            'C': 0.1,
            'D': 0.2
        })
        self.text = 'ABBCD'

    def test_encode_when_called_return_code(self):
        code = self.encoder.encode(self.text)

        self.assertEqual(code, '0 01 1 1 100 0111')
