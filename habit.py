""" Theses are the classes and docstrings for our project."""

import argparse
import sys

class User:
    """ This is the class for the user 

    Attributes: 
        user_id: This is the user id 
        username (str): this is the username for the user
        password (str): the password of the user
    """
    def __init__(self, user_id, username, password):
        self.user_id = user_id 
        self.username = username
        self.password = password
        
class Manager:
    """ This is the class for managing the users and storing them in a 
        dictionary
    
        Attributes: 
            users: this is for storing the users
    """
    def __init__(self):
        self.users = {}
        
class Habit:
    """ This represents a habit
    
        Attributes: 
            user_id: the user id of the user 
            name: 
            category: 
            frequency: 
            streak: 
    """
    def __init__(self, user_id, name, category, frequency, streak: str=None, database=" "):
        self.user_id = user_id
        self.name = name
        self.category = category
        self.frequency = frequency
        self.streak = 0
        
class Tracker:
    """ It manages habits and stores them 
    """
    def __init__(self):
        self.habits = {}
        
    def add_habit(self, habit):
        self.habits[habit.id] = habit


def parse_args(args_list):
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to the text file')
    return parser.parse_args(args_list)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print(args.path)