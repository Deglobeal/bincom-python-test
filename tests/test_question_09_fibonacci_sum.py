import unittest

from questions.question_09_fibonacci_sum import (
    fibonacci_sequence,
    sum_first_50_fibonacci,
)


class TestFibonacciSum(unittest.TestCase):
    def test_first_ten_numbers(self):
        self.assertEqual(
            fibonacci_sequence(10),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
        )

    def test_generates_50_numbers(self):
        self.assertEqual(len(fibonacci_sequence(50)), 50)

    def test_sum_of_first_50(self):
        self.assertEqual(sum_first_50_fibonacci(), 20365011073)

    def test_zero_count(self):
        self.assertEqual(fibonacci_sequence(0), [])

    def test_rejects_negative_count(self):
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)


if __name__ == "__main__":
    unittest.main()
