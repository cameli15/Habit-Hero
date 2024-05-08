import unittest
from unittest.mock import patch, MagicMock
import login  

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case by patching the database connection and creating mock objects.
        """
        self.patcher_db = patch('login.sqlite3.connect') 
        self.mock_db = self.patcher_db.start()
        self.addCleanup(self.patcher_db.stop)

        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_db.return_value = self.mock_conn
        self.mock_conn.cursor.return_value = self.mock_cursor

    @patch('login.questionary.text')
    @patch('login.questionary.password')
    @patch('login.hashlib.sha256')
    def test_register_user(self, mock_sha256, mock_password, mock_text):
        """
        Test the register_user function.
        """
        # Set up mock objects and side effects
        mock_text.side_effect = [MagicMock(ask=lambda: 'User Test'), MagicMock(ask=lambda: 'testing')]
        mock_password.return_value = MagicMock(ask=lambda: 'password123')
        hashed_password = MagicMock(hexdigest=lambda: 'hashed_password')
        mock_sha256.return_value = hashed_password

        # Mock database response
        self.mock_cursor.fetchall.return_value = []

        # Call the function to be tested
        login.register_user()

        # Assert database interactions
        self.mock_cursor.execute.assert_called_with("INSERT INTO users VALUES (?, ?, ?)",
                                                    ('User Test', 'testing', 'hashed_password'))
        self.mock_conn.commit.assert_called()

    def test_get_user(self):
        """
        Test the get_user function.
        """
        # Mock database response
        self.mock_cursor.fetchall.return_value = [('User Test', 'testing', 'hashed_password')]

        # Call the function to be tested
        user = login.get_user('testing')

        # Assert database interactions and returned user object
        self.mock_cursor.execute.assert_called_with("SELECT * FROM users WHERE username = 'testing'")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testing')

    @patch('login.questionary.text')
    @patch('login.check_password')
    def test_login(self, mock_check_password, mock_text):
        """
        Test the login function.
        """
        # Set up mock objects and side effects
        mock_text.return_value = MagicMock(ask=lambda: 'testing')

        # Mock database response
        self.mock_cursor.fetchall.return_value = [('User Test', 'testing', 'hashed_password')]

        # Call the function to be tested
        login.login()

        # Assert function calls
        mock_check_password.assert_called_with('hashed_password')

    @patch('login.questionary.password')
    def test_check_password(self, mock_password):
        """
        Test the check_password function.
        """
        # Set up mock objects and side effects
        mock_password.return_value = MagicMock(ask=lambda: 'password123')
        mock_password.return_value = MagicMock(ask=lambda: 'password123')
        self.patcher_hash = patch('login.hashlib.sha256')
        mock_hash = self.patcher_hash.start()
        mock_hash.return_value.hexdigest.return_value = 'hashed_password'

        # Call the function to be tested
        login.check_password('hashed_password')

        # Assert function calls
        self.assertEqual(mock_password.call_count, 1)
        self.patcher_hash.stop()

if __name__ == '__main__':
    unittest.main()
