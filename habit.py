""" Theses are the classes and docstrings for our project."""

import argparse
import sys

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        
class Manager:
    def __init__(self):
        self.users = {}
        
class Habit:
    def __init__(self, user_id, name, category, frequency, streak: str=None, database=" "):
        self.user_id = user_id
        self.name = name
        self.category = category
        self.frequency = frequency
        self.streak = 0
        
class Tracker:
    def __init__(self):
        self.habits = {}
        
    def add_habit(self, habit):
        self.habits[habit.id] = habit


def parse_args(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to the text file')
    return parser.parse_args(args_list)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print(args.path)