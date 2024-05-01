# this file will contain our User Class that will be where users can track their habits, create new ones, delete, and possibly choose from pre-exisiting ones

import sqlite3
import habit
from PyInquirer import prompt

class User:
    """
    A user class to represent a user of HabitHero.
    
    Attributes: 
        firstname (str) - first name of user
        lastname (str) - last name of user
        username (str) - username of user
        password (str) - password of user
        
    Methods:

    """
    # Init method
    def __init__(self, firstname, lastname, username, password):
        """
        Initializes User class and sets up the attributes for the user.
        
        Parameters:
            self (str)
            firstname (str) - first name of user
            lastname (str) - last name of user
            username (str) - username of user
            password (str) - password of user
        """
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password

        db_path = Path(__file__).parent / "main_db.db"
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        
#store data into database
    def store_in_db(self):
      """Stores user data into DB when registering"""
        
    # store habit into database
    def store_habit_in_db(self, new_habit):

# function to retrieve habit from the db
    def retrieve_habit(self, habit_name):

# maybe we can have preset choices for users to choose from so we can demonstrate the program, we don't need it if you guys dont think its neccesary
    def choose_preset_habit(self):

     # where user can create a habit
    def create_habit(self):

# where user can delete a habit out of the database, again idk if we'll 100% need this but just as an option
    def delete_habit(self):

# function that prints out all of the data within the database so users can see their progress
    def show_all(self):

# shows user current streak overview of all their habits stored by frequency
    def current_streak_overview(self):




        
    
