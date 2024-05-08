import unittest
from unittest.mock import patch
import re
from database_manager import launch_database

class TestDatabaseOperations(unittest.TestCase):
    @patch('database_manager.sqlite3.connect')
    def test_launch_database_creates_tables(self, mock_connect):
        """
        Test if the launch_database function creates the required tables.
        
        This test mocks the connection to the database to ensure that the function 
        correctly executes the SQL statements for creating tables and commits the changes.
        """
        # Set up mock objects
        mock_conn = mock_connect.return_value.__enter__.return_value
        mock_cursor = mock_conn.cursor.return_value
    
        # Call the function to be tested
        launch_database()
        
        # Define patterns for expected SQL statements
        expected_patterns = [
            r"CREATE TABLE IF NOT EXISTS users \(\s*firstname TEXT,\s*username TEXT PRIMARY KEY,\s*password TEXT\s*\)",
            r"CREATE TABLE IF NOT EXISTS habits \(\s*habit_name TEXT,\s*member TEXT,\s*category TEXT,\s*frequency TEXT,\s*creation_timestamp DATETIME\s*\)",
            r"CREATE TABLE IF NOT EXISTS habit_data \(\s*habit_name TEXT,\s*frequency TEXT,\s*member TEXT,\s*creation_timestamp DATETIME\s*\)"
        ]

        # Extract actual SQL statements executed by the mock cursor
        actual_statements = [call[1][0] for call in mock_cursor.mock_calls if call[0] == 'execute']
        
        # Check if each expected pattern matches at least one actual SQL statement
        for pattern in expected_patterns:
            self.assertTrue(any(re.search(pattern, stmt.replace('\n', ' ').replace('    ', ' ')) for stmt in actual_statements),
                            f"Pattern not found: {pattern}")

        # Check if commit was called once
        mock_conn.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
