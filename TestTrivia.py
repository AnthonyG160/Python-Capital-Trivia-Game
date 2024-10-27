import unittest
from unittest.mock import patch, MagicMock
import sqlite3
from TriviaGame import TriviaGame

class TestTriviaGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test database."""
        cls.game = TriviaGame(':memory:')

    def test_insert_questions(self):
        """Test if questions are inserted into the database."""
        initial_count = self.game.cursor.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
        self.game.insert_questions()
        new_count = self.game.cursor.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
        self.assertGreater(new_count, initial_count)

    def test_check_if_table_is_empty(self):
        """Test if the check_if_table_is_empty function works correctly."""
        self.game.insert_questions()
        self.assertFalse(self.game.check_if_table_is_empty())

    def test_get_random_question(self):
        """Test if get_random_question returns a question."""
        self.game.insert_questions()
        question = self.game.get_random_question()
        self.assertIsNotNone(question)
        self.assertEqual(len(question), 7)

    @patch('builtins.input', side_effect=['5'])
    def test_get_valid_number_input_valid(self, mock_input):
        """Test if valid number input is correctly returned."""
        self.assertEqual(self.game.get_valid_number_input("Enter a number", 1, 20), 5)

    @patch('builtins.input', side_effect=['25', '10'])
    def test_get_valid_number_input_invalid(self, mock_input):
        """Test if invalid input is handled properly."""
        self.assertEqual(self.game.get_valid_number_input("Enter a number", 1, 20), 10)

if __name__ == '__main__':
    unittest.main()