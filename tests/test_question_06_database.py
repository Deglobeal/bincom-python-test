"""Integration tests for Question 6 using PostgreSQL."""

import unittest

from questions.dress_data import get_color_frequencies
from questions.question_06_database import (
    create_table,
    fetch_color_frequencies,
    get_database_connection,
    save_color_frequencies,
)


class TestPostgreSQLColorFrequencies(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = get_database_connection()
        create_table(cls.connection)
        save_color_frequencies(cls.connection)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_all_12_color_labels_are_stored(self):
        records = fetch_color_frequencies(self.connection)
        self.assertEqual(len(records), 12)

    def test_stored_frequencies_match_source_data(self):
        records = dict(fetch_color_frequencies(self.connection))
        self.assertEqual(records, dict(get_color_frequencies()))

    def test_saving_again_does_not_create_duplicates(self):
        saved_count = save_color_frequencies(self.connection)
        records = fetch_color_frequencies(self.connection)

        self.assertEqual(saved_count, 12)
        self.assertEqual(len(records), 12)

    def test_blue_frequency_is_30(self):
        records = dict(fetch_color_frequencies(self.connection))
        self.assertEqual(records["BLUE"], 30)


if __name__ == "__main__":
    unittest.main()
