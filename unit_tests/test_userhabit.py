import unittest
from unittest.mock import patch, MagicMock
from userhabit import User, Habit
from datetime import datetime

class TestHabit(unittest.TestCase):
    def test_habit_initialization(self):
        """Test initialization of Habit instance."""
        creation_time = datetime.now()
        habit = Habit('Running', 'test_user', 'Health', 'Daily', creation_time)
        self.assertEqual(habit.habit_name, 'Running')
        self.assertEqual(habit.member, 'test_user')
        self.assertEqual(habit.category, 'Health')
        self.assertEqual(habit.frequency, 'Daily')
        self.assertEqual(habit.creation_timestamp, creation_time)

class TestUser(unittest.TestCase):
    def setUp(self):
        """Setup for all tests."""
        patcher = patch('userhabit.sqlite3.connect')
        self.mock_connect = patcher.start()
        self.addCleanup(patcher.stop)

        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connect.return_value = self.mock_conn
        self.mock_conn.cursor.return_value = self.mock_cursor

        self.user = User('Test', 'test123', 'password')
    
    def test_user_initialization(self):
        """Test initialization of User instance."""
        self.assertEqual(self.user.firstname, 'Test')
        self.assertEqual(self.user.username, 'test123')
        self.assertEqual(self.user.password, 'password')
    
    def test_store_in_db(self):
        """Test storing user in the database."""
        self.user.store_in_db()
        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users VALUES (?, ?, ?)",
            ('Test', 'test123', 'password')
        )
        self.mock_conn.commit.assert_called_once()

    def test_check_habit_exists(self):
        """Test checking if a habit exists."""
        self.mock_cursor.fetchall.return_value = [
            ('Running', 'test123', 'Health', 'Daily', '2024-05-07 12:00:00')
        ]
        habit = self.user.check_habit('Running')
        self.assertIsNotNone(habit)
        self.assertEqual(habit.habit_name, 'Running')
        self.mock_cursor.execute.assert_called_with(
            "SELECT * FROM habits WHERE habit_name = 'Running' AND member = 'test123';"
        )
    
    def test_show_all(self):
        """Test showing all habits."""
        self.mock_cursor.fetchall.return_value = [('Running',)]
        habits = self.user.show_all()
        self.assertEqual(habits, ['Running'])
        self.mock_cursor.execute.assert_called_with(
            "SELECT habit_name FROM habits WHERE member = 'test123';"
        )

    def test_store_habit_in_db(self):
        """Test storing a habit in the database."""
        habit = Habit('Running', 'test123', 'Health', 'Daily', datetime.now())
        self.user.store_habit_in_db(habit)
        self.mock_cursor.execute.assert_called_with(
            "INSERT INTO habits VALUES (?, ?, ?, ?, ?)",
            ('Running', 'test123', 'Health', 'Daily', habit.creation_timestamp)
        )
        self.mock_conn.commit.assert_called()

if __name__ == '__main__':
    unittest.main()