import unittest

from questions.question_07_bonus_recursive_search import recursive_search


class TestRecursiveSearch(unittest.TestCase):
    def test_finds_number(self):
        self.assertEqual(recursive_search([10, 20, 30, 40], 30), 2)

    def test_returns_minus_one_when_missing(self):
        self.assertEqual(recursive_search([10, 20, 30], 50), -1)

    def test_finds_first_duplicate(self):
        self.assertEqual(recursive_search([5, 2, 5], 5), 0)

    def test_handles_empty_list(self):
        self.assertEqual(recursive_search([], 10), -1)

    def test_handles_first_element(self):
        self.assertEqual(recursive_search([7, 8, 9], 7), 0)


if __name__ == "__main__":
    unittest.main()
