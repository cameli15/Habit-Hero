"""docstring or line comments here explaining the code"""
# make sure to add line comments throughout the code too

import sqlite3
from pathlib import Path

def launch_database():
    """Creating and launching the database"""
    db_path = Path(__file__).resolve().parent / 'habithero_db.db'
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT,
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                habit_name TEXT,
                member TEXT,
                category TEXT,
                frequency TEXT,
                creation_timestamp DATETIME
            )
        """)
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
