""" This is our login.py file. This is where we will create our database and manage user data and activity"

import user
import hashlib
import sqlite3
import questionary
from os.path import join, dirname, abspath

# launch database and establish a connection
def launch database():
  """ Contains 3 tables: users, habits, and habit_data that will contain all of our programs data into a database"""
  db_path = join(dirname(abspath(__file__)), 'main_db.db')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT,
                lastname TEXT,
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
            CREATE TABLE IF NOT EXISTS habit_data (
                habit_name TEXT,
                frequency TEXT,
                member TEXT,
                creation_timestamp DATETIME
            )
        """)

# user interaction for registration (will use questionary)
def register_user():
  """users will give their first name, username, password, and we will check their password using hashlib"""
    firstname = questionary.text("What is your first name? ",
                                 validate=None).ask()
    # code for the rest will go here

    # we have to check if their username is original and pull user data from our user file and class
    new_user = user.User(firstname, username, password)
    users = get_user(username)
    if users:
        print("\nThis username already exists. Try again!\n")
        register_user()

    else:
        new_user.store_in_db()
        print("\nRegistration successful!\n")

  # function to retreive user data from the database
  def retrieve_user(username):
    """"pull user info from database"""

  # user login process that will also connect to the main.py file
def login():
    """ function that lets users login"""
    user_name = questionary.text("Enter username:").ask()
    users = get_user(user_name)
    
    if users: 
        check_password(users.password)
        return users
    else: 
        print("\nWrong username! Try again\n")
        login()

# Function to check user's password
def check_password(password):
    """function to check the user password"""
    password_input = questionary.password("Enter your password: ").ask()
    password_input = hashlib.sha256(password_input.encode('utf-8')).hexdigest()
    if password_input == password:
        print("\nLogin successful!\n")
    else:
        print("\nPassword incorrect. Try again!\n")
        check_password(password)
  
  
  
