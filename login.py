import userhabit
import hashlib
import sqlite3
import questionary
from os.path import join, dirname, abspath

# launch database and establish a connection
def launch_database():
    """Contains 3 tables: users, habits, and habit_data that will contain all of 
        our program's data into a database
        
        Side effects:
            Creating the tables if they were not already created
    """
    db_path = join(dirname(abspath(__file__)), 'main_db.db')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # create the table for storing users and their information
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT,
                lastname TEXT,
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)

        # creating the table for habits
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                habit_name TEXT,
                member TEXT,
                category TEXT,
                frequency TEXT,
                creation_timestamp DATETIME
            )
        """)

        # creating the table for habit and its data
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
    """ This function allows the user to register an account for them

        Side effects: 
            Creating the firstname, username, and password and putting it in 
            the database
    """
    firstname = questionary.text("What is your first name? ",
                                 validate=None).ask()
    username = questionary.text("What is your username? ",
                                validate=None).ask()
    password = questionary.password("What is your password? ",
                                    validate=None).ask()
    password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # create a new entry for a new user 
    new_user = userhabit.User(firstname, username, password)
    user = get_user(username)

    # checking if the username is already in the database
    if user:
        print("\nThis username already exists. Try again!\n")
        register_user()
    else:
        new_user.store_in_db()
        print("\nRegistration successful!\n")


def get_user(username):
    """This is to find the user through checking for their username in the 
        database
    
    Args: 
        username(str): the username of the user

    Returns: 
        user: the user's password, first name and username
        None
    """
    db_path = join(dirname(abspath(__file__)), 'main_db.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    #using a sql query to go through the user table to find the username
    cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
    list_of_users = cur.fetchall()

    # takes the user's information and returns it 
    if len(list_of_users) > 0:
        firstname, username, password = list_of_users[0]
        user = userhabit.User(firstname, username, password)
        return user
    else:
        return None


def login():
    """This is for the user to login with their username and password
    
    Returns: 
        user: the user's password, first name and username 
    """
    user_name = questionary.text("Enter username:").ask()
    user = get_user(user_name)

    # checking to see if the input of the user and the password connected to the 
    # user's information in the datbase is correct    
    if user: 
        check_password(user.password)
        return user
    else: 
        print("\nWrong username! Try again\n")
        login()


def check_password(password):
    """This is to check if the input by the user matches the password that 
        that is saved into the database. If it doesn't match, then it will loop 
        until it does.
    """

    password_input = questionary.password("Enter your password: ").ask()
    password_input = hashlib.sha256(password_input.encode('utf-8')).hexdigest()

    # this is to check if it is the right password
    if password_input == password:
        print("\nLogin successful!\n")
    else:
        print("\nPassword incorrect. Try again!\n")
        check_password(password)
