import unittest
from unittest.mock import patch, MagicMock
from userhabit import User, Habit
from datetime import datetime

class TestHabit(unittest.TestCase):
    def test_habit_initialization(self):
        creation_time = datetime.now()
        habit = Habit('Running', 'test_user', 'Health', 'Daily', creation_time)
        self.assertEqual(habit.habit_name, 'Running')
        self.assertEqual(habit.member, 'test_user')
        self.assertEqual(habit.category, 'Health')
        self.assertEqual(habit.frequency, 'Daily')
        self.assertEqual(habit.creation_timestamp, creation_time)

class TestUser(unittest.TestCase):
    @patch('userhabit.sqlite3.connect')
    def test_store_in_db(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        
        user = User('Test', 'test123', 'password')
        user.store_in_db()
        
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users VALUES (?, ?, ?)",
            ('Test', 'test123', 'password')
        )
        mock_conn.commit.assert_called_once()

    @patch('userhabit.sqlite3.connect')
    def test_check_habit_exists(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            ('Running', 'test123', 'Health', 'Daily', '2024-05-07 12:00:00')
        ]

        user = User('Test', 'test123', 'password')
        habit = user.check_habit('Running')

        self.assertIsNotNone(habit)
        self.assertEqual(habit.habit_name, 'Running')
        mock_cursor.execute.assert_called_with(
            "SELECT * FROM habits WHERE habit_name = 'Running' AND member = 'test123';"
        )

if __name__ == '__main__':
    unittest.main()
