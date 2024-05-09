import unittest
from unittest.mock import patch, MagicMock, Mock
from userhabit import User, Habit
from datetime import datetime

class TestHabit(unittest.TestCase):
    def test_habit_initialization(self):
        """
        Test initialization of Habit instance.
        """
        # Create a habit instance
        creation_time = datetime.now()
        habit = Habit('Running', 'test_user', 'Health', 'Daily', creation_time)
        
        # Assert attributes
        self.assertEqual(habit.habit_name, 'Running')
        self.assertEqual(habit.member, 'test_user')
        self.assertEqual(habit.category, 'Health')
        self.assertEqual(habit.frequency, 'Daily')
        self.assertEqual(habit.creation_timestamp, creation_time)

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Setup for all tests.
        """
        # Patch database connection
        patcher = patch('userhabit.sqlite3.connect')
        self.mock_connect = patcher.start()
        self.addCleanup(patcher.stop)

        # Mock database connection and cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connect.return_value = self.mock_conn
        self.mock_conn.cursor.return_value = self.mock_cursor

        # Create a user instance
        self.user = User('Test', 'test123', 'password')
    
    def test_user_initialization(self):
        """
        Test initialization of User instance.
        """
        # Assert attributes
        self.assertEqual(self.user.firstname, 'Test')
        self.assertEqual(self.user.username, 'test123')
        self.assertEqual(self.user.password, 'password')
    
    def test_store_in_db(self):
        """
        Test storing user in the database.
        """
        # Call store_in_db method
        self.user.store_in_db()
        
        # Assert database interactions
        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users VALUES (?, ?, ?)",
            ('Test', 'test123', 'password')
        )
        self.mock_conn.commit.assert_called_once()

    def test_check_habit_exists(self):
        """
        Test checking if a habit exists.
        """
        # Mock database response
        self.mock_cursor.fetchall.return_value = [
            ('Running', 'test123', 'Health', 'Daily', '2024-05-07 12:00:00')
        ]
        
        # Call check_habit method
        habit = self.user.check_habit('Running')
        
        # Assert returned habit object and database interactions
        self.assertIsNotNone(habit)
        self.assertEqual(habit.habit_name, 'Running')
        self.mock_cursor.execute.assert_called_with(
            "SELECT * FROM habits WHERE habit_name = 'Running' AND member = 'test123';"
        )
    
    def test_show_all(self):
        """
        Test showing all habits.
        """
        # Mock database response
        self.mock_cursor.fetchall.return_value = [('Running',)]
        
        # Call show_all method
        habits = self.user.show_all()
        
        # Assert returned habits list and database interactions
        self.assertEqual(habits, ['Running'])
        self.mock_cursor.execute.assert_called_with(
            "SELECT habit_name FROM habits WHERE member = 'test123';"
        )

    def test_store_habit_in_db(self):
        """
        Test storing a habit in the database.
        """
        # Create a habit instance
        habit = Habit('Running', 'test123', 'Health', 'Daily', datetime.now())
        
        # Call store_habit_in_db method
        self.user.store_habit_in_db(habit)
        
        # Assert database interactions
        self.mock_cursor.execute.assert_called_with(
            "INSERT INTO habits VALUES (?, ?, ?, ?, ?)",
            ('Running', 'test123', 'Health', 'Daily', habit.creation_timestamp)
        )
        self.mock_conn.commit.assert_called()

    @patch("userhabit.questionary.text")
    @patch("userhabit.questionary.select")
    def test_adding_habit(self, mock_select, mock_text): 
        """
        Test adding a habit to the user
        """
        mock_text.return_value.ask.return_value = "Lifting"
        mock_select.return_value.ask.side_effect = ["Health", "Daily"]

        #Call the add_habit with the new habit 
        new_habit = self.user.add_habit() 
        
        # Asserting that the habit exists
        self.assertIsInstance(new_habit, Habit)
        self.assertEqual(new_habit.habit_name, "Lifting")
        self.assertEqual(new_habit.member, 'test123')
        self.assertEqual(new_habit.category, 'Health')
        self.assertEqual(new_habit.frequency, 'Daily')
        self.assertIsInstance(new_habit.creation_timestamp, datetime)
    
    @patch("userhabit.questionary.text")
    @patch("userhabit.questionary.select")
    def test_delete_habit(self, mock_text, mock_select): 
        """
        Testing the delete habit function
        """
        mock_text.return_value.ask.return_value = "Lifting"
        mock_select.return_value.ask.side_effect = ["Health", "Daily"]

        #Call the add_habit with the new habit 
        new_habit = self.user.add_habit()
        self.user.show_all()
        self.user.delete_habit()

        # Checking to see if it exists anymore
        self.assertIsNot(new_habit, Habit)
    
    @patch("userhabit.questionary.text")
    @patch("userhabit.questionary.select")
    def test_habit_completed(self, mock_text, mock_select): 
        """
        Testing the habit completed function
        """
        # Set the return value for the mocked text function
        mock_text.return_value.ask.return_value = "Lifting"
        mock_select.return_value.ask.side_effect = ["Health", "Daily"]

        #Call the add_habit with the new habit 
        new_habit = self.user.add_habit()
        
        # Reset mock calls to ignore calls made during add_habit
        mock_text.reset_mock()
        mock_select.reset_mock()

        # Set the return value for the mocked text function to the habit added
        mock_text.return_value.ask.return_value = new_habit.habit_name
        
        # Call the habit_completed method
        self.user.habit_completed()

        self.assertEqual(mock_text.call_count, 0)

if __name__ == '__main__':
    unittest.main()
