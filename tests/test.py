import unittest

from ..src.main import calculate


class TestCalculator(unittest.TestCase):
    def test_sum_simple(self):
        self.assertEqual(calculate("2 + 2"), 4)

    def test_sum_with_negatives(self):
        self.assertEqual(calculate("-1 + 2"), 1)

    def test_sum_large_numbers(self):
        self.assertEqual(calculate("100000 + 250000"), 350000)

    def test_sum_with_zero(self):
        self.assertEqual(calculate("0 + 5"), 5)

    def test_subtract_simple(self):
        self.assertEqual(calculate("5 - 2"), 3)

    def test_subtract_with_negatives(self):
        self.assertEqual(calculate("-3 - 2"), -5)

    def test_subtract_large_numbers(self):
        self.assertEqual(calculate("500000 - 123456"), 376544)

    def test_subtract_resulting_in_zero(self):
        self.assertEqual(calculate("10 - 10"), 0)

    def test_multiply_simple(self):
        self.assertEqual(calculate("3 * 4"), 12)

    def test_multiply_with_negatives(self):
        self.assertEqual(calculate("-3 * 4"), -12)

    def test_multiply_large_numbers(self):
        self.assertEqual(calculate("2000 * 3000"), 6000000)

    def test_multiply_with_zero(self):
        self.assertEqual(calculate("0 * 9999"), 0)

    def test_divide_simple(self):
        self.assertEqual(calculate("8 / 2"), 4)

    def test_divide_with_negatives(self):
        self.assertEqual(calculate("-10 / 2"), -5)

    def test_divide_large_numbers(self):
        self.assertEqual(calculate("1000000 / 100"), 10000)

    def test_divide_resulting_in_fraction(self):
        self.assertEqual(calculate("7 / 3"), 7 / 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate("10 / 0")

    def test_combined_operations_1(self):
        self.assertEqual(calculate("2 + 3 * 4"), 14)

    def test_combined_operations_2(self):
        self.assertEqual(calculate("(2 + 3) * 4"), 20)

    def test_combined_operations_3(self):
        self.assertEqual(calculate("10 / 2 + 3"), 8)

    def test_combined_operations_4(self):
        self.assertEqual(calculate("10 / (2 + 3)"), 2)

    def test_invalid_syntax_1(self):
        with self.assertRaises(SyntaxError):
            calculate("2 + ")

    def test_invalid_syntax_2(self):
        with self.assertRaises(SyntaxError):
            calculate("5 * ")

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            calculate("5 + a")

    def test_complex_operation_1(self):
        self.assertEqual(calculate("3 + 5 * 2 - 8 / 4"), 9)

    def test_complex_operation_2(self):
        self.assertEqual(calculate("10 + 2 * 6 / (4 - 2)"), 16)

    def test_complex_operation_3(self):
        self.assertEqual(calculate("100 / 10 + 5 * (7 - 3)"), 30)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            calculate("")

    def test_only_whitespace(self):
        with self.assertRaises(ValueError):
            calculate("    ")

    def test_multiple_whitespaces(self):
        self.assertEqual(calculate("3  +  4 *  2 "), 11)

    def test_repeated_addition(self):
        self.assertEqual(calculate("1 + 1 + 1 + 1 + 1"), 5)

    def test_repeated_subtraction(self):
        self.assertEqual(calculate("10 - 2 - 2 - 2"), 4)

    def test_repeated_multiplication(self):
        self.assertEqual(calculate("2 * 2 * 2 * 2"), 16)

    def test_repeated_division(self):
        self.assertEqual(calculate("100 / 2 / 2"), 25)

    def test_decimal_addition(self):
        self.assertEqual(calculate("2.5 + 3.5"), 6.0)

    def test_decimal_subtraction(self):
        self.assertEqual(calculate("5.5 - 2.2"), 3.3)

    def test_decimal_multiplication(self):
        self.assertEqual(calculate("2.2 * 3.0"), 6.6)

    def test_decimal_division(self):
        self.assertEqual(calculate("7.5 / 2.5"), 3.0)

    def test_negative_decimal_addition(self):
        self.assertEqual(calculate("-2.5 + 3.5"), 1.0)

    def test_negative_decimal_subtraction(self):
        self.assertEqual(calculate("-5.5 - 2.5"), -8.0)

    def test_negative_decimal_multiplication(self):
        self.assertEqual(calculate("-2.2 * 3.0"), -6.6)

    def test_negative_decimal_division(self):
        self.assertEqual(calculate("-7.5 / 2.5"), -3.0)

    def test_large_expression(self):
        expression = "1" + "+1" * 1000
        self.assertEqual(calculate(expression), 1001)

    def test_large_numbers_with_overflow(self):
        self.assertEqual(
            calculate("999999999999 * 999999999999"), 999999999998000000000001
        )

    def test_precision_with_floats(self):
        self.assertAlmostEqual(calculate("1.0000000001 + 2.0000000002"), 3.0000000003)


if __name__ == "__main__":
    unittest.main()
