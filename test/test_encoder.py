from unittest import TestCase

from src.encoder.encoder import Encoder


class TestEncoder(TestCase):
    def setUp(self) -> None:
        class FakeEncoder(Encoder):
            def encode(self, text: str, calculate_prob: bool = False) -> str:
                super().encode(text, calculate_prob)
                return 'fake'
        self.initial_probs = {
            'A': 0.6,
            'B': 0.4
        }
        self.fake_encoder = FakeEncoder(self.initial_probs)

    def test_encode_when_not_calculate_probabilities_verify_initial_probs(self):
        self.fake_encoder.encode('AAAB')

        self.assertEqual(self.initial_probs, self.fake_encoder.probabilities)

    def test_encode_when_calculate_probabilities_verify_new_probs(self):
        self.fake_encoder.encode('AAAB', calculate_prob=True)
        expected_probs = {
            'A': 0.75,
            'B': 0.25
        }

        self.assertEqual(expected_probs, self.fake_encoder.probabilities)

    def test_calculate_prob_intervals_when_called_verify_interval_probabilities(self):
        test_cases = [
            {
                'interval': (0.0, 1.0),
                'result': {
                    'A': (0.0, 0.6),
                    'B': (0.6, 1.0)
                }
            },
            {
                'interval': (0.6, 1.0),
                'result': {
                    'A': (0.6, 0.84),
                    'B': (0.84, 1.0)
                }
            }
        ]
        for test_case in test_cases:
            interval = test_case['interval']
            with self.subTest(interval=interval):
                self.fake_encoder._calculate_prob_intervals(interval)
                self.assertEqual(test_case['result'], self.fake_encoder.prob_intervals)
