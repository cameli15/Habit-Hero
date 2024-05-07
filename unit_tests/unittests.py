import sqlite3 
import unittest
from unittest.mock import MagicMock, patch
from io import StringIO 
from login import register_user, get_user
from pathlib import Path
import database_manager
import hashlib
import userhabit

# testing the database launch
class TestLaunchDatabase(unittest.TestCase):
    def test_tables_created(self):
        # Call the function to create tables
        database_manager.launch_database()
        
        # Connect to the database
        db_path = Path(__file__).resolve().parent / 'habithero_db.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if users table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        
        # Check if habits table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='habits'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        
        # Check if habit_data table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='habit_data'")
        result = cursor.fetchone()
        self.assertIsNotNone(result)
        
        # Close the connection
        conn.close()

if __name__ == '__main__':
    unittest.main()
