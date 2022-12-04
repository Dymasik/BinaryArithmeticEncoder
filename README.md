# Install

1. `virtualenv venv`
2. `pip install -r requirements.txt`

# Run
To test encoder: `python src/main.py --file src/example/test_text.txt --probabilities src/example/test_probabilities.txt`

* `file` - path to file with text to encode
* `probabilities` - path to file with symbols probabilities (you can skip specifing it, so probabilities will be autocalculated based on input text)

# Test

Current unit test coverage is **99%**.

1. Run `python test.py`
2. * To run coverage: `coverage run test.py`
    * `coverage report -m`
    * To generate coverage HTML (optional): `coverage html`
