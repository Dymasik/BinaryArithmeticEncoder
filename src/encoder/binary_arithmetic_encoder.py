from src.encoder.encoder import Encoder


class BinaryArithmeticEncoder(Encoder):
    def encode(self, text: str, calculate_prob: bool = False) -> str:
        super().encode(text, calculate_prob)
        current_interval = (0.0, 1.0)
        self._calculate_prob_intervals(current_interval)
        bit_count = 0
        code = ''
        for char in text:
            current_interval = self.prob_intervals[char]
            while True:
                if current_interval[0] < 0.5 and current_interval[1] < 0.5:
                    code += '0' + ('1' * bit_count if bit_count > 0 else '')
                    code += ' '
                    bit_count = 0
                    current_interval = (current_interval[0] * 2.0, current_interval[1] * 2.0)
                elif current_interval[0] >= 0.5 and current_interval[1] >= 0.5:
                    code += '1' + ('0' * bit_count if bit_count > 0 else '')
                    code += ' '
                    bit_count = 0
                    current_interval = ((current_interval[0] - 0.5) * 2.0, (current_interval[1] - 0.5) * 2.0)
                elif current_interval[0] >= 0.25 and current_interval[1] < 0.75:
                    bit_count += 1
                    current_interval = ((current_interval[0] - 0.25) * 2.0, (current_interval[1] - 0.25) * 2.0)
                else:
                    break
            self._calculate_prob_intervals(current_interval)
        bit_count += 1
        if current_interval[0] < 0.25:
            code += '0' + ('1' * bit_count if bit_count > 0 else '')
        else:
            code += '1' + ('0' * bit_count if bit_count > 0 else '')
        return code
