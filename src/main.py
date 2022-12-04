from argparse import ArgumentParser
from src.encoder.binary_arithmetic_encoder import BinaryArithmeticEncoder


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--file', type=str, help="Path to file to encode")
    parser.add_argument('--probabilities', type=str, help='Path to file with symbols probabilities')
    args = parser.parse_args()

    calculate_probabilities = True
    probabilities = {}
    if args.probabilities:
        with open(args.probabilities, 'r') as prob_file:
            line = prob_file.readline()
            while line:
                line_parts = line.split()
                probabilities[line_parts[0]] = float(line_parts[1])
                line = prob_file.readline()
        print(f"Read probabilities: {probabilities}")
        calculate_probabilities = False
    encoder = BinaryArithmeticEncoder(probabilities)
    with open(args.file, 'r') as target_file:
        text = target_file.read()
        print(f"Read text: {text}")
        code = encoder.encode(text, calculate_prob=calculate_probabilities)
    print(f"Code: {code}")
        