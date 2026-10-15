import unittest
from unittest.mock import patch

from questions.question_08_binary_to_decimal import (
    binary_to_decimal,
    generate_random_binary_number,
)


class TestBinaryToDecimal(unittest.TestCase):
    def test_converts_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("1010"), 10)

    def test_converts_all_zeros(self):
        self.assertEqual(binary_to_decimal("0000"), 0)

    def test_preserves_four_digits(self):
        with patch(
            "questions.question_08_binary_to_decimal.random.randint",
            return_value=3,
        ):
            self.assertEqual(generate_random_binary_number(), "0011")

    def test_rejects_wrong_length(self):
        with self.assertRaises(ValueError):
            binary_to_decimal("101")

    def test_rejects_invalid_digits(self):
        with self.assertRaises(ValueError):
            binary_to_decimal("1021")


if __name__ == "__main__":
    unittest.main()
