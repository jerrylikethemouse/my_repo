# Calculator Class

The Calculator class is a Python implementation of basic arithmetic operations with additional validation features. It supports addition, subtraction, multiplication, and division, ensuring robust handling of various input types.

## Features

- **Addition:** Adds two numbers.
- **Subtraction:** Subtracts one number from another.
- **Multiplication:** Multiplies two numbers.
- **Division:** Divides one number by another.

## Usage

Instantiate the Calculator class and use its methods for arithmetic operations.

```python
from calculator import Calculator

# Create an instance of the Calculator class
calculator = Calculator()

# Example usage
result = calculator.add(x=5, y=3)
print(result)  # Output: 8
```

## Test Program
The test_calculator.py file contains a comprehensive test suite for the Calculator class. It covers various scenarios, including positive cases, error handling, and edge cases, using the unittest framework.

## Running Tests
Execute the test program to ensure the correctness of the Calculator class.
```
python test_calculator.py
```
## Dependencies
No external dependencies are required. The Calculator class is implemented in pure Python.

## Contribution
Feel free to contribute by submitting issues or pull requests.

Happy calculating!
