
import sqlite3
from pathlib import Path

def launch_database():
    """
    Initializes and sets up a local SQLite database for our program.

    Tables:
        - users: contains users information (name, username, password)
        - habits: stores the habits, category, and frequency of users
        - habit_data: logs the data of each habit for users
    """
    db_path = Path(__file__).resolve().parent / 'habithero_db.db'
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        #create users table to store data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT,
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)

        #create habits table to store habits
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                habit_name TEXT,
                member TEXT,
                category TEXT,
                frequency TEXT,
                creation_timestamp DATETIME
            )
        """)

        #creates habit_data table to store habit data
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habit_data (
                habit_name TEXT,
                frequency TEXT,
                member TEXT,
                creation_timestamp DATETIME
            )
        """)
        
    conn.commit()
    conn.close()
