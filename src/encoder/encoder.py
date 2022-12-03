from abc import ABC, abstractmethod
from typing import Dict, Tuple


class Encoder(ABC):
    def __init__(self, probabilities: Dict[str, float] = {}) -> None:
        self.probabilities = probabilities
        self.prob_intervals: Dict[str, Tuple[float, float]] = {}

    @abstractmethod
    def encode(self, text: str, calculate_prob: bool = False) -> str:
        if not self.probabilities or calculate_prob:
            self._calculate_probabilities(text)
        pass

    def _calculate_probabilities(self, text: str):
        chars_count = {}
        for char in text:
            char_count = chars_count.get(char, 0)
            chars_count[char] = char_count + 1
        self.probabilities = {}
        total_count = len(text)
        for char in chars_count:
            self.probabilities[char] = chars_count[char] / total_count

    def _calculate_prob_intervals(self, interval: Tuple[float, float]):
        lower_bound = interval[0]
        interval_len = interval[1] - interval[0]
        for index, char in enumerate(self.probabilities):
            upper_bound = lower_bound + (self.probabilities[char] * interval_len) if index != len(self.probabilities) else interval[1]
            self.prob_intervals[char] = (lower_bound, upper_bound)
            lower_bound = upper_bound

