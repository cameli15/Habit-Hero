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

        #Connecting to database
        self.conn = sqlite3.connect('main.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute = ('''CREATE TABLE IF NOT EXISTS habits 
                                (habit_name TEXT, member TEXT, category TEXT, frequency TEXT, creation_timestamp TEXT)''')
        self.conn.commit ()
    #Adding values to database
    def add_to_table(self):
        self.cursor.execute = ("INSERT INTO habits VALUES(?,?,?,?,?)", (self.habit_name, self.member, self.category, self.frequency, str (self.creation_timestamp)))
        self.conn.commit ()
    #Closing the database connection
    def close_connection(self):
        self.conn.close ()
