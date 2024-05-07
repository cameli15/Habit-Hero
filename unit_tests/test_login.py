import unittest
from unittest.mock import patch, MagicMock
import login  

class TestUserManagement(unittest.TestCase):
    def setUp(self):
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
        mock_text.side_effect = [MagicMock(ask=lambda: 'John Doe'), MagicMock(ask=lambda: 'johndoe')]
        mock_password.return_value = MagicMock(ask=lambda: 'password123')
        hashed_password = MagicMock(hexdigest=lambda: 'hashed_password')
        mock_sha256.return_value = hashed_password

        self.mock_cursor.fetchall.return_value = []

        login.register_user()

        self.mock_cursor.execute.assert_called_with("INSERT INTO users VALUES (?, ?, ?)",
                                                    ('John Doe', 'johndoe', 'hashed_password'))
        self.mock_conn.commit.assert_called()

    def test_get_user(self):
        self.mock_cursor.fetchall.return_value = [('John Doe', 'johndoe', 'hashed_password')]

        user = login.get_user('johndoe')

        self.mock_cursor.execute.assert_called_with("SELECT * FROM users WHERE username = 'johndoe'")

        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'johndoe')

    @patch('login.questionary.text')
    @patch('login.check_password')
    def test_login(self, mock_check_password, mock_text):
        mock_text.return_value = MagicMock(ask=lambda: 'johndoe')

        self.mock_cursor.fetchall.return_value = [('John Doe', 'johndoe', 'hashed_password')]

        login.login()

        mock_check_password.assert_called_with('hashed_password')

    @patch('login.questionary.password')
    def test_check_password(self, mock_password):
        mock_password.return_value = MagicMock(ask=lambda: 'password123')
        mock_password.return_value = MagicMock(ask=lambda: 'password123')
        self.patcher_hash = patch('login.hashlib.sha256')
        mock_hash = self.patcher_hash.start()
        mock_hash.return_value.hexdigest.return_value = 'hashed_password'

        login.check_password('hashed_password')

        self.assertEqual(mock_password.call_count, 1)
        self.patcher_hash.stop()

if __name__ == '__main__':
    unittest.main()
