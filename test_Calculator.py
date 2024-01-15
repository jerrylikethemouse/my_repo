import unittest

from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_result_type(self):
        result = self.calculator.add(x=10, y=5)
        self.assertTrue(isinstance(result, (int, float)))

        result = self.calculator.add(x=20.5, y=3)
        self.assertTrue(isinstance(result, (int, float)))

    def test_add_numbers_returns_sum(self):
        result = self.calculator.add(x=20, y=60) 
        self.assertEqual(20 + 60, result) 

        result = self.calculator.add(x=20.56, y=60.89)
        self.assertEqual(20.56 + 60.89, result) 

    def test_add_string_type_error(self):
        with self.assertRaises(TypeError) as context:
            result = self.calculator.add("Hello", "World")
            self.assertNotIsInstance(result, str)

    def test_add_string_numbers_returns_sum(self):
        result = self.calculator.add(x="50", y="60.7")
        self.assertEqual(50 + 60.7, result)
        
        result = self.calculator.add(x=50, y="60.7")
        self.assertEqual(50 + 60.7, result)
        
        result = self.calculator.add(x="50", y=60.7)
        self.assertEqual(50 + 60.7, result)
    
    def test_add_negative_string_numbers_returns_sum(self):
        result = self.calculator.add(x="-50", y="60.7")
        self.assertEqual(-50 + 60.7, result)
        
        result = self.calculator.add(x=50, y="-60.7")
        self.assertEqual(50 + (-60.7), result)
        
        result = self.calculator.add(x="-50", y=60.7)
        self.assertEqual((-50) + 60.7, result)

    def test_add_zero_values_returns_sum(self):
        result = self.calculator.add(x=0, y=0)
        self.assertEqual(0 + 0, result)

    def test_add_decimal_values_returns_sum(self):
        result = self.calculator.add(x=.5, y=.3)
        self.assertEqual(0.5 + 0.3, result)

    def test_add_negative_zero_and_positive_numbers_returns_sum(self):
        result = self.calculator.add(x=-0, y=10)
        self.assertEqual(-0 + 10, result)

    def test_multiply_with_fractions(self):
        result = self.calculator.multiply(x=2/3, y=1/4)
        self.assertEqual(2/3 + 1/4, result)

#subtract unit tests
        
    def test_subtract_result_type(self):
        result = self.calculator.subtract(x=10, y=5)
        self.assertTrue(isinstance(result, (int, float)))

        result = self.calculator.subtract(x=20.5, y=3)
        self.assertTrue(isinstance(result, (int, float)))
        
    def test_subtract_numbers_returns_difference(self):
        result = self.calculator.subtract(x=60, y=20)
        self.assertEqual(60 - 20, result)

        result = self.calculator.subtract(x=60.89, y=20.56)
        self.assertEqual(60.89 - 20.56, result)

    def test_subtract_string_type_error(self):
        with self.assertRaises(TypeError) as context:
            result = self.calculator.subtract("Hello", "World")
            self.assertNotIsInstance(result, str)
    
    def test_subtract_with_negative_inputs(self):
        result = self.calculator.subtract(x=-10, y=-10)
        self.assertEqual(0, result)

        result = self.calculator.subtract(x=10, y=-10)
        self.assertEqual(20, result)
        
        result = self.calculator.subtract(x=-10, y=10)
        self.assertEqual(-20, result)

    def test_for_zero_inputs_subtract(self):
        result = self.calculator.subtract(x=0, y=0)
        self.assertEqual(0, result)

        result = self.calculator.subtract(x=0, y=10)
        self.assertEqual(-10, result)

        result = self.calculator.subtract(x=5, y=0)
        self.assertEqual(5, result)
    
    def test_subtract_with_large_inputs(self):
        result = self.calculator.subtract(x=1e10, y=1e5)
        self.assertEqual(1e10 - 1e5, result)

        result = self.calculator.subtract(x=-1e10, y=-1e5)
        self.assertEqual(-1e10 + 1e5, result)

    def test_subtract_string_numbers_returns_sum(self):
        result = self.calculator.subtract(x="50", y="60.7")
        self.assertEqual(50 - 60.7, result)
        
        result = self.calculator.subtract(x=50, y="60.7")
        self.assertEqual(50 - 60.7, result)
        
        result = self.calculator.subtract(x="50", y=60.7)
        self.assertEqual(50 - 60.7, result)
    
    def test_subtract_with_fractions(self):
        result = self.calculator.subtract(x=2/3, y=1/4)
        self.assertEqual(2/3 - 1/4, result)

# multiply unit tests
        
    def test_multiply_result_type(self):
        result = self.calculator.multiply(x=10, y=5)
        self.assertTrue(isinstance(result, (int, float)))

        result = self.calculator.multiply(x=20.5, y=3)
        self.assertTrue(isinstance(result, (int, float)))
        
    def test_multiply_numbers_returns_difference(self):
        result = self.calculator.multiply(x=60, y=20)
        self.assertEqual(60 * 20, result)

        result = self.calculator.multiply(x=60.89, y=20.56)
        self.assertEqual(60.89 * 20.56, result)

    def test_multiply_string_type_error(self):
        with self.assertRaises(TypeError) as context:
            result = self.calculator.multiply("Hello", "World")
            self.assertNotIsInstance(result, str)
    
    def test_multiply_with_negative_inputs(self):
        result = self.calculator.multiply(x=-10, y=-10)
        self.assertEqual((-10) * (-10), result)

        result = self.calculator.multiply(x=10, y=-10)
        self.assertEqual(10 * (-10), result)
        
        result = self.calculator.multiply(x=-10, y=10)
        self.assertEqual((-10) * 10, result)

    def test_for_zero_inputs_multiply(self):
        result = self.calculator.multiply(x=0, y=0)
        self.assertEqual(0, result)

        result = self.calculator.multiply(x=0, y=10)
        self.assertEqual(0, result)

        result = self.calculator.multiply(x=5, y=0)
        self.assertEqual(0, result)
    
    def test_multiply_with_large_inputs(self):
        result = self.calculator.multiply(x=1e10, y=1e5)
        self.assertEqual(1e10 * 1e5, result)

        result = self.calculator.multiply(x=1e10, y=-1e5)
        self.assertEqual(1e10 * -1e5, result)

        result = self.calculator.multiply(x=-1e10, y=-1e5)
        self.assertEqual(-1e10 * -1e5, result)

    def test_multiply_string_numbers_returns_sum(self):
        result = self.calculator.multiply(x="50", y="60.7")
        self.assertEqual(50 * 60.7, result)
        
        result = self.calculator.multiply(x=50, y="60.7")
        self.assertEqual(50 * 60.7, result)
        
        result = self.calculator.multiply(x="50", y=60.7)
        self.assertEqual(50 * 60.7, result)

    def test_multiply_with_small_numbers(self):
        result = self.calculator.multiply(x=.00000001, y=.00000001)
        self.assertEqual(.00000001*.00000001, result)

        result = self.calculator.multiply(x=1e-10, y=1e-5)
        self.assertEqual(1e-10 * 1e-5, result)

    def test_multiply_with_fractions(self):
        result = self.calculator.multiply(x=2/3, y=1/4)
        self.assertEqual(2/3 * 1/4, result)

# divide unit tests
        
    def test_divide_result_type(self):
        result = self.calculator.divide(x=10, y=5)
        self.assertTrue(isinstance(result, (int, float)))

        result = self.calculator.divide(x=20.5, y=3)
        self.assertTrue(isinstance(result, (int, float)))
        
    def test_divide_numbers_returns_difference(self):
        result = self.calculator.divide(x=60, y=20)
        self.assertEqual(60 / 20, result)

        result = self.calculator.divide(x=60.89, y=20.56)
        self.assertEqual(60.89 / 20.56, result)

    def test_divide_string_type_error(self):
        with self.assertRaises(TypeError) as context:
            result = self.calculator.divide("Hello", "World")
            self.assertNotIsInstance(result, str)
    
    def test_divide_with_negative_inputs(self):
        result = self.calculator.divide(x=-10, y=-10)
        self.assertEqual((-10) / (-10), result)

        result = self.calculator.divide(x=10, y=-10)
        self.assertEqual(10 / (-10), result)
        
        result = self.calculator.divide(x=-10, y=10)
        self.assertEqual((-10) / 10, result)

    def test_for_zero_inputs_divide(self):
        with self.assertRaises(ZeroDivisionError):
            result = self.calculator.divide(x=0, y=0)

        result = self.calculator.divide(x=0, y=10)
        self.assertEqual(0/10, result)

        with self.assertRaises(ZeroDivisionError):
            result = self.calculator.divide(x=5, y=0)
    
    def test_divide_with_large_inputs(self):
        result = self.calculator.divide(x=1e10, y=1e5)
        self.assertEqual(1e10 / 1e5, result)

        result = self.calculator.divide(x=1e10, y=-1e5)
        self.assertEqual(1e10 / -1e5, result)

        result = self.calculator.divide(x=-1e10, y=-1e5)
        self.assertEqual(-1e10 / -1e5, result)

    def test_divide_string_numbers_returns_sum(self):
        result = self.calculator.divide(x="50", y="60.7")
        self.assertEqual(50 / 60.7, result)
        
        result = self.calculator.divide(x=50, y="60.7")
        self.assertEqual(50 / 60.7, result)
        
        result = self.calculator.divide(x="50", y=60.7)
        self.assertEqual(50 / 60.7, result)

    def test_divide_with_small_numbers(self):
        result = self.calculator.divide(x=.00000001, y=.00000001)
        self.assertEqual(.00000001/.00000001, result)

        result = self.calculator.divide(x=1e-10, y=1e-5)
        self.assertEqual(1e-10 / 1e-5, result)

    def test_divide_with_fractions(self):
        result = self.calculator.divide(x=2/3, y=1/4)
        self.assertEqual((2/3) / (1/4), result)


if __name__ == '__main__':
    unittest.main()
