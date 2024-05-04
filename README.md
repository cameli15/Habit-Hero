# Habit-Hero
Habit Hero is a Python program designed to help users manage their habits efficiently. It allows users to track their habits, add new ones, mark them as completed, and delete them as needed. The program utilizes SQLite for database management and provides a user-friendly interface for interaction.

Features

-User Registration and Login: Users can register for an account with their first name, username, and password. Existing users can log in using their username and password.

-Habit Management: Users can add new habits, delete existing ones, and mark habits as completed.

-Database Management: The program uses SQLite to store user information, habits, and habit completion data.

-User Interface: The program provides a simple and intuitive command-line interface for users to interact with.

Files

-userhabit.py: This file defines the Habit class, which represents a habit and its attributes as well as the User class, which represents a user and their attributes. The habit class includes methods for interacting with the SQLite database to manage habits and the User class ncludes methods for user registration, login, and managing habits.

-login.py: This file contains functions for user registration, login, and password verification.

-database_manager.py: This file includes a function to initialize and set up the SQLite database for the program. It creates tables for storing user information, habits, and habit completion data.

-main.py: This is the main entry point for the Habit Hero program. It orchestrates the interaction between users, their habits, and the database. It provides a user-friendly interface for managing habits.

Walkthrough

To use Habit Hero, follow these steps:

-Clone the repository to your local machine.

-Install the required dependencies by running pip install -r requirements.txt.

-Run the program by executing python main.py.

-Follow the on-screen prompts to register/login and manage your habits.
