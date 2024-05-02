""" This is the Habit Class."""

import sqlite3


class Habit:
    """Class used to represent habits."""
    
    # this is where our init method will go
    def __init__(self, habit_name, member, category, frequency, creation_timestamp):
        """
        Initialize an instance of the Habit Class, creating the initial attributes and establishing a database connection.
        
        Parameters:
            habit_name (str) - name of habit
            member (str) - indivdual member associated with a habit
            category (str) - category habit is in ('health', 'work', 'leisure')
            frequency (str) - frequency of habit ('daily' or 'weekly')
            creation_timestamp (datetime) - date/time when habit was created
        
        Attributes:
            self.habit_name (str) - stores the name of the habit
            self.member (str) - stores member's habit
            self.category (str) - stores category of habit
            self.frequency (str) - stores frequency of habit
            self.creation_timestamp (datetime) - stores date/time creation of habit
            
        This method sets up a connection to the SQLite database. It initializes a cursor for executing database operations.  
        """
        self.habit_name = habit_name
        self.member = member
        self.category = category
        self.frequency = frequency
        self.creation_timestamp = creation_timestamp

    def get_db_connection():
        db_path = Path(__file__).resolve().parent / 'main_db.db'
        return sqlite3.connect(str(db_path))

    def save(self):
        conn = Habit.get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO habits (habit_name, member, category, frequency, creation_timestamp) VALUES (?, ?, ?, ?, ?)",
                           (self.habit_name, self.member, self.category, self.frequency, self.creation_timestamp))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
