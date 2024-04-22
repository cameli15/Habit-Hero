""" Theses are the classes and docstrings for our project."""

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