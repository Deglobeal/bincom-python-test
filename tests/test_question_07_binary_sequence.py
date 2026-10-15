"""Tests for the binary-sequence puzzle."""

import unittest

from questions.question_07_binary_sequence import transform_binary_sequence


class TestBinarySequence(unittest.TestCase):
    def test_matches_assessment_example(self):
        binary = "0101101011101011011101101000111"
        expected = "0000000000100000000100000000001"

        self.assertEqual(transform_binary_sequence(binary), expected)

    def test_marks_third_and_subsequent_consecutive_ones(self):
        self.assertEqual(transform_binary_sequence("011110"), "000110")

    def test_sequences_shorter_than_three_ones_produce_zeros(self):
        self.assertEqual(transform_binary_sequence("0110110"), "0000000")

    def test_rejects_invalid_characters(self):
        with self.assertRaises(ValueError):
            transform_binary_sequence("01012")

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            transform_binary_sequence("")


if __name__ == "__main__":
    unittest.main()
