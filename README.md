# Habit-Hero: Final Project Program
Habit Hero is a our Python program designed for our final INST 326 project. We designed it with the intention of helping users manage their habits efficiently. It allows users to track their habits, add new ones, mark them as completed, and delete them as needed. The program utilizes SQLite for database management and provides a user-friendly interface for interaction with the use of the library questionary.

**Features**

* User Registration and Login: Users can register for an account with their first name, username, and password. Existing users can log in using their username and password.

* Habit Management: Users can add new habits, delete existing ones, and mark habits as completed.

* Database Management: The program uses SQLite to store user information, habits, and habit completion data.

* User Interface: The program provides a simple and intuitive command-line interface for users to interact with using questionary.

## Files 

**Main Files for Program**
* <ins>userhabit.py</ins>: This file defines the Habit class, which represents a habit and its attributes as well as the User class, which represents a user and their attributes. The habit class includes methods for interacting with the SQLite database to manage habits and the User class ncludes methods for user registration, login, and managing habits.

* <ins>login.py</ins>: This file contains functions for user registration, login, and password verification through code lines of questionary.

* <ins>database_manager.py</ins>: This file includes a function to initialize and set up the SQLite database for the program. It creates tables for storing user information, habits, and habit completion data.

* <ins>main.py</ins>: This is the main entry point for the Habit Hero program. It orchestrates the interaction between users, their habits, and the database. It provides a user-friendly interface for managing habits.

**Unit Test Folder**

*This folder contains our unit tests for the different classes, methods, and functions within our program's code. 
To run these tests, make sure that they are in the same parent directory as the main files of the program.*

* test_database_manager.py
* test_userhabit.py
* test_login.py
* test_main.py



**Habit Hero Data Folder**

*This folder contains sample data collected in our habithero_db.db from testing our program. There are three different tables created and stored.*
*You must have sqlite3 installed to run the database and view its contents*

* habits.db: contains all users habits that they add
* habit_data.db: contains all the progress of users as they mark their habits as complete
* users.db: contains all registered users information
* habithero_db.db: overall database that contains all of the tables.


## Walkthrough

To use Habit Hero, follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running pip install questionary and sqlite3 should already be a part of your Python if not, you can install it following these instructions:
https://stackoverflow.com/questions/19530974/how-can-i-add-the-sqlite3-module-to-python

3. Run the program by first executing the other files *(database_manager.py, userhabit.py and, login.py)* to initialize the database and classes.
   
5. Then to run the program for use, run the *main.py* file and use the program from the command line.

6. Follow the on-screen prompts to register/login and manage your habits.
   - Once you register an account, you must reexecute the main.py file and continue adding or managing your habits.


## Works Cited
*Sources used as reference for libraries and modules used throughout our code.*

- https://docs.python.org/3/library/sqlite3.html
  
- https://stackoverflow.com/questions/21005822/what-does-os-path-abspathos-path-joinos-path-dirname-file-os-path-pardir
  
- https://questionary.readthedocs.io/en/stable/pages/types.html#text
  
- https://docs.python.org/3/library/hashlib.html 
- https://docs.python.org/3/library/os.path.html 
- https://pypi.org/project/questionary/#features
- https://www.browserstack.com/guide/unit-testing-python#:~:text=To%20run%20these%20test%20cases,python%20%2Dm%20unittest%20%2Dv.


### INST 326 (0201) - Group 17
- Cinthia Contreras
- Lakshya Sajal Kumar
- Linaly Jaqueline Miyamoto
- Evan Carr
