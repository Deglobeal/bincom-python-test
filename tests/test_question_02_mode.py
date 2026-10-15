"""Tests for Question 2: mode."""

import unittest

from questions.question_02_mode import calculate_mode


class TestMode(unittest.TestCase):
    def test_blue_is_the_most_frequent_color(self):
        modes, frequency = calculate_mode()
        self.assertEqual(modes, ["BLUE"])
        self.assertEqual(frequency, 30)


if __name__ == "__main__":
    unittest.main()
