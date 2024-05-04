import questionary
import login
import database_manager


def program_menu():
    """
    This is to display the meny for the Habit Hero program. This function prompts
    the user for initial actions, such as registration or login.
    
    Returns: 
        user: the user's first name, username and password 
        None: If the users chooses to exit
    """
    database_manager.launch_database() #connects file to database
    
    print("\nHello! Welcome to Habit Hero!\n")
    initial_message = questionary.select(
        "Is this your first time here?", choices=[
            "Yes! First time!",
            "Nope! :D"
        ]).ask()
    
    if initial_message == "Yes! First time!":
        action = questionary.select(
            "Welcome, Let's get you started with your registration!",
            choices=[
                "Register! :D",
                "Exit :("
            ]).ask()
        
        if action == "Register! :D":
            user = login.register_user()  
            if user:
                print(f"\nWelcome!\n")
                return user
            else:
                return None
        elif action == "Exit :(":
            print("Exiting the program.")
            return None
    
    elif initial_message == "Nope! :D":
        action = questionary.select(
            "Welcome back! What would you like to do?",
            choices=[
                "Login",
                "Exit :("
            ]).ask()
        if action == "Login":
            user = login.login()
            if user:
                print(f"\nWelcome back, {user.firstname}!\n")
                return user
        elif action == "Exit :(":
            print("Exiting the program.")
            return None


def main():
    """
    This is the main function to run the Habit Hero program. It handles the flow
    of the program, such as displaying the menu and executing the user's actions
    
    Raises: 
        Exception e: If an error occurs during program execution
    """
    try:
        user = program_menu() # starts the program
        if not user:
            return  # User chose to exit or failed to login/register

        # Display the main meny
        while True:
            menu_question = questionary.select("What would you like to do?",
                                               choices=[
                                                   "Add, Delete, or Mark a Habit as complete",
                                                   "View Habits",
                                                   "Exit Habit Hero"
                                               ]).ask()
            if menu_question == "View Habits":
                print("Let's take a look!\n")
                # Display all habits for the user
                user.show_all() 
        
            elif menu_question == "Add, Delete, or Mark a Habit as complete":
                habit_choice = questionary.select("What would you like to do?",
                                            choices=[
                                                "Add Habit",
                                                "Delete Habit",
                                                "Mark a habit as completed! Yay!"
                                            ]).ask()
        
                if habit_choice == "Add Habit":
                    print("Great! Let's get a new habit started!")
                    new_habit = user.add_habit()
                    user.store_habit_in_db(new_habit)
                
                elif habit_choice == "Delete Habit":
                    user.delete_habit()
                
                elif habit_choice == "Mark a habit as completed! Yay!":
                    user.habit_completed()
        
            elif menu_question == "Exit Habit Hero":
                print(f"\nBye {user.firstname}! We hope you come back soon!\n")
                break  
        
    except Exception as e:
        print(f"An error occurred: {e}")
            
            
if __name__ == "__main__":
    main()
