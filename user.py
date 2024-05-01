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

        #db connection should go here
#store data into database
    def store_in_db(self):
      """Stores user data into DB when registering"""

        
    
