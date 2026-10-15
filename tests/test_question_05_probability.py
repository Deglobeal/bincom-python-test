"""Tests for Question 5: probability of RED."""

import unittest

from questions.question_05_probability import calculate_red_probability


class TestRedProbability(unittest.TestCase):
    def test_probability_matches_expected_result(self):
        self.assertAlmostEqual(calculate_red_probability(), 9 / 95)

    def test_probability_is_between_zero_and_one(self):
        probability = calculate_red_probability()
        self.assertGreaterEqual(probability, 0)
        self.assertLessEqual(probability, 1)


if __name__ == "__main__":
    unittest.main()
