#install PyInquirer using pip install PyInquirer in command line
#login.py is another file that will be our main file for the program

from PyInquirer import prompt
import login

# creates database
login.launch_database()

# program starts and we'll implement an opening message
welcome_message = "\n" # write into message

print(welcome_message)

# this is where users will login/register using PyInquirer

questions = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'Is this your first time using HabitHero or are you a returning user?',
        'choices': [
            'Register',
            'Login'
        ]
    }
]

answer = prompt(questions)

if answer['action'] == 'Login':
    user = login.login()
    print("We're happy to see you back!\n")
elif answer['action'] == 'Register':
    print("\nWelcome! Since it's your first time here, let's get you set up.\n")
    login.register_user()
    print("\nPlease log in\n")
    user = login.login()
    
# if its a newly registered user, insert choices from habits or allow them to create?
# whatever is best for the project

#create menu for the beginning of the program
def menu():
    """
    Main menu of our program.
    
    Asks user what they want to do from a list of choices.
    """
    # ex: mark habit as complete, view habits, create habit, delete habit, exit
