
import sqlite3
from pathlib import Path

def launch_database():
    """
    Initializes and sets up a local SQLite database for our program.

    Tables:
        - users: contains users information (name, username, password)
        - habits: stores the habits, category, and frequency of users
        - progress: logs the progress of each habit for users
    """
    db_path = Path(__file__).resolve().parent / 'habithero_db.db'
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # creating the table for users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT,
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)

        #creating the table for habits
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                habit_name TEXT,
                member TEXT,
                category TEXT,
                frequency TEXT,
                creation_timestamp DATETIME
            )
        """)

        # creating the table for progress
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                habit_name TEXT,
                frequency TEXT,
                member TEXT,
                creation_timestamp DATETIME
            )
        """)
        
    conn.commit()
    conn.close()
