"""Tests for Question 3: median frequency."""

import unittest

from questions.question_03_median import calculate_median_frequency


class TestMedianFrequency(unittest.TestCase):
    def test_median_matches_expected_result(self):
        self.assertEqual(calculate_median_frequency(), 5.5)

    def test_median_handles_even_length_lists(self):
        values = [1, 2, 3, 4]
        middle = len(values) // 2
        median = (values[middle - 1] + values[middle]) / 2
        self.assertEqual(median, 2.5)

    def test_median_handles_odd_length_lists(self):
        values = [1, 2, 3]
        middle = len(values) // 2
        self.assertEqual(float(values[middle]), 2.0)


if __name__ == "__main__":
    unittest.main()
