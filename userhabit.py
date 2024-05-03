
import sqlite3
from datetime import datetime
from pathlib import Path
import questionary 

class Habit:
    """
    Class used to represent habits.
    
    Attributes:
        habit_name (str) - name of habit
        member (str) - indivdual member associated with a habit
        category (str) - category habit is in ('health', 'work', 'leisure')
        frequency (str) - frequency of habit ('daily' or 'weekly')
        creation_timestamp (datetime) - date/time when habit was created
    """
    
    def __init__(self, habit_name, member, category, frequency, creation_timestamp):
        """
        Initialize an instance of the Habit class and creating the initial attributes
        
        Parameters:
            habit_name (str) - name of habit
            member (str) - indivdual member associated with a habit
            category (str) - category habit is in ('health', 'work', 'leisure')
            frequency (str) - frequency of habit ('daily' or 'weekly')
            creation_timestamp (datetime) - date/time when habit was created
        """
        self.habit_name = habit_name
        self.member = member
        self.category = category
        self.frequency = frequency
        self.creation_timestamp = creation_timestamp
    
        # makes a path to the database
        db_path = Path(__file__).parent / "habithero_db.db"
        self.conn = sqlite3.connect(str(db_path))
        self.cur = self.conn.cursor()


class User:
    """This is the class of the user and functions related to the user
    
    Attributes: 
        firstname (str): the first name of the user 
        username (str): the username of the user 
        password (str): the password of the user 
    """
    def __init__(self, firstname, username, password):
        """ Intializing the user entry with the following attributes: 
            firstname, username and password

        Attributes: 
            Please see the class attributes above. 
        
        """
        self.firstname = firstname
        self.username = username
        self.password = password
        
        # makes a path to the database
        db_path = Path(__file__).parent / "habithero_db.db"
        self.conn = sqlite3.connect(str(db_path))
        self.cur = self.conn.cursor()

    def store_in_db(self):
        """ 
        This function put the user entry and all of the information related 
        to the user entry into the habithero using SQL commands
        
        Args: 
            self: the user entry 
        """

        # inserts the user entry to the user table in the database
        self.cur.execute("INSERT INTO users VALUES (?, ?, ?)",
                         (self.firstname, self.username, self.password))
        self.conn.commit()
        
    def check_habit(self, habit_name):
        """
        This function checks to see if the user has been doing that habit
        under the username.

        Returns: 
            habits: the habit entry associated with the user in the database
            None: this is just in case, the function couldn't find the habit for
                the user 
        """
        self.cur.execute(f"SELECT * FROM habits WHERE habit_name = '{habit_name}' AND member = '{self.username}';")
        habits_in_db = self.cur.fetchall()

        # checking if the habit does exist for the user
        if len(habits_in_db) > 0:
            habit_name, member, category, frequency, creation_timestamp = habits_in_db[0]
            habits = Habit(habit_name, member, category, frequency, creation_timestamp)
            return habits
        else:
            return None    
        
    def add_habit(self):
        """
        This function allows the user to add a new habit for their account
        as well as adding the habit into the database for future reference.

        Args: 
            self: the username entry and the habit entry associated with it

        Returns: 
            new_habit: the new habit entry created by the user
        """
        
        habit_name = questionary.text("What is your new habit?",
                                      validate=None).ask()
        
        member = self.username
        
        category = questionary.select("Which category does your habit belong in?:",
                                      choices=[
                                          "Health",
                                          "Work",
                                          "Leisure"
                                      ]).ask()
        
        frequency = questionary.select("Will this be a daily or weekly habit?",
                                       choices=[
                                           "Daily",
                                           "Weekly"
                                       ]).ask()
        
        creation_timestamp = datetime.now()
        
        #creates the new habit entry
        new_habit = Habit(habit_name, member, category, frequency, creation_timestamp)
        current_habits = self.check_habit(habit_name)

        # checks to see if the habit entry already exists
        if current_habits:
            print("\nYou already have this habit!\n")
            self.add_habit()
        else:
            print("\nSuccessfully created a new habit!\n")
            return new_habit
        
    def delete_habit(self):
        """This function allows the user to delete a habit from their account"""
        habit_name = questionary.text("Which habit would you like to delete?",
                                      validate=None).ask()
        
        #check to see if the habit exists in the database 
        current_habits = self.check_habit(habit_name)
        if current_habits:
            self.cur.execute(f"DELETE FROM habits WHERE habit_name = '{habit_name}' AND member = '{self.username}';")
            self.cur.fetchall()
            self.conn.commit()
            print(f"'{habit_name}' successfully deleted!")
        else:
            print("\nThis habit doesn't exist!\n")
    
    def habit_completed(self):
        """
        This function allows user to log in their entry for whether or not 
        they did their habit for the day. 
        
        Args: 
            self: this is the user entry and the habit entry associated with it. 
        """
    
        habit_completed = questionary.text("What habit do you want to mark as completed? ",
                                       validate=None).ask()
        
        current_habits = self.check_habit(habit_completed)

        if current_habits:
            creation_timestamp = datetime.now()
            self.cur.execute("INSERT INTO progress VALUES(?, ?, ?, ?)",
                             (current_habits.habit_name, current_habits.frequency, self.username,
                              creation_timestamp))
            self.conn.commit()
            print("You've completed your habit. Congrats!")
        else:
            print("Oops! This isn't one of your habits.")
    
    def show_all(self):
        """ 
        This allows the user to see the habits that the user put into the 
        database
        
        Args: 
            self: this is the user entry and the habit entry associated with it.
        
        Returns: 
            habits: the habit entry associated with the suer
        """
        self.cur.execute(f"SELECT habit_name FROM habits WHERE member = '{self.username}';")
        items = self.cur.fetchall()
        habits = []
        for item in items:
            habits.append(item[0])
        print(habits)
        return habits
            
            
    def store_habit_in_db(self, new_habit):
        """
        This function allows us to store the habit into the database
        
        Args: 
            self: this is the user entry and the habit entry associated with it.

        Returns: 
            new_habit: this is the new habit entry that must be added into the 
                database
        """
        self.cur.execute("INSERT INTO habits VALUES (?, ?, ?, ?, ?)",
                    (new_habit.habit_name, new_habit.member, new_habit.category, new_habit.frequency, new_habit.creation_timestamp))
        self.conn.commit()
