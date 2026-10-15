"""Tests for Question 1: mean frequency."""

import unittest

from questions.question_01_mean import calculate_mean_frequency
from questions.dress_data import get_color_frequencies, get_all_colors


class TestMeanFrequency(unittest.TestCase):
    def test_mean_frequency_matches_expected_result(self):
        self.assertAlmostEqual(calculate_mean_frequency(), 95 / 12)

    def test_dataset_contains_95_entries(self):
        self.assertEqual(len(get_all_colors()), 95)

    def test_dataset_contains_12_unique_labels(self):
        self.assertEqual(len(get_color_frequencies()), 12)


if __name__ == "__main__":
    unittest.main()
