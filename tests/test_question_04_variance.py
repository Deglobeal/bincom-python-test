"""Tests for Question 4: population variance."""

import unittest

from questions.question_04_variance import calculate_population_variance


class TestPopulationVariance(unittest.TestCase):
    def test_variance_matches_expected_result(self):
        self.assertAlmostEqual(
            calculate_population_variance(),
            63.24305555555556,
        )

    def test_variance_is_non_negative(self):
        self.assertGreaterEqual(calculate_population_variance(), 0)


if __name__ == "__main__":
    unittest.main()
