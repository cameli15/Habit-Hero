#install PyInquirer using pip install PyInquirer in command line
#login.py is another file that will be our main file for the program

from PyInquirer import prompt
import login
import user

# creates database
login.launch_database()

# program starts and we'll implement an opening message
welcome_message = "\nHello! Welcome to Habit Hero!\n" # write into message

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
    menu_choices = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'What do you want to do?',
            'choices': [
                'Create, Delete or Mark a Habit as completed',
                'Activity Overview',
                'View Habits',
                Separator(),
                'Exit Program'
            ]
        }
    ]

    second_question = prompt(menu_choices)['action']

    if second_question == 'Create, Delete or Mark a Habit as completed':
        habit_choices = [
            {
                'type': 'list',
                'name': 'habit_action',
                'message': 'Do you want to:',
                'choices': [
                    'Create a new habit',
                    'Delete habit',
                    'Mark a habit as completed'
                ]
            }
        ]
        habit_question = prompt(habit_choices)['habit_action']

        if habit_question == 'Create a new habit':
            print("Let's create a new habit.\n")
            new_habit = user.create_habit()
            user.store_habit_in_db(new_habit)
            print("\nWhat do you want to do next?\n")
            menu()

        elif habit_question == 'Delete habit':
            user.delete_habit()
            print("\nWhat do you want to do next?\n")
            menu()
             elif habit_question == 'Mark a habit as completed':
            user.is_completed()  
            print("\nWhat do you want to do next?\n")
            menu()

        elif second_question == 'Exit Program':
            print(f"\nSee you soon, {user.firstname}!\n")   
