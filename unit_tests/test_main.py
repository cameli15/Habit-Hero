import unittest
from unittest.mock import patch, MagicMock, call
import main

class TestMainProgram(unittest.TestCase):
    @patch('main.questionary.select')
    @patch('main.login.register_user')
    @patch('main.database_manager.launch_database')
    def test_program_menu_first_time_register(self, mock_launch_database, mock_register_user, mock_select):
        """Test program menu with first-time registration."""
        mock_select.side_effect = [
            MagicMock(ask=lambda: "Yes! First time!"),  
            MagicMock(ask=lambda: "Register! :D")      
        ]
        mock_register_user.return_value = MagicMock(firstname="Test")

        user = main.program_menu()

        mock_launch_database.assert_called_once()
        mock_select.assert_has_calls([
            call(
                "Is this your first time here?", choices=["Yes! First time!", "Nope! :D"]
            ),
            call(
                "Welcome, Let's get you started with your registration!", choices=["Register! :D", "Exit :("]
            )
        ])
        self.assertEqual(user.firstname, "Test")


    @patch('main.questionary.select')
    @patch('main.login.login')
    @patch('main.database_manager.launch_database')
    def test_program_menu_returning_user_login(self, mock_launch_database, mock_login, mock_select):
        """Test program menu with a returning user login."""
        mock_select.side_effect = [
            MagicMock(ask=lambda: "Nope! :D"),  
            MagicMock(ask=lambda: "Login")      
        ]
        mock_login.return_value = MagicMock(firstname="Test")

        user = main.program_menu()

        mock_launch_database.assert_called_once()
        mock_select.assert_has_calls([
            call(
                "Is this your first time here?", choices=["Yes! First time!", "Nope! :D"]
            ),
            call(
                "Welcome back! What would you like to do?", choices=["Login", "Exit :("]
            )
        ])
        self.assertEqual(user.firstname, "Test")
        
        
class TestMainFunction(unittest.TestCase):
    @patch('main.questionary.select')
    @patch('main.program_menu', return_value=MagicMock(firstname="John", show_all=MagicMock(), 
                                                       add_habit=MagicMock(), store_habit_in_db=MagicMock(), 
                                                       delete_habit=MagicMock(), habit_completed=MagicMock()))
    
    
    def test_main_view_habits_and_exit(self, mock_program_menu, mock_select):
        """Test main function where user views habits and exits."""
        mock_select.side_effect = [
            MagicMock(ask=lambda: "View Habits"), 
            MagicMock(ask=lambda: "Exit Habit Hero") 
        ]

        main.main()

        user = mock_program_menu.return_value
        user.show_all.assert_called_once()
        mock_select.assert_has_calls([
            call("What would you like to do?", choices=["Add, Delete, or Mark a Habit as complete", "View Habits", "Exit Habit Hero"]),
            call("What would you like to do?", choices=["Add, Delete, or Mark a Habit as complete", "View Habits", "Exit Habit Hero"])
        ])

    @patch('main.questionary.select')
    @patch('main.program_menu', return_value=MagicMock(firstname="John", show_all=MagicMock(), 
                                                       add_habit=MagicMock(return_value="New Habit"), 
                                                       store_habit_in_db=MagicMock(), delete_habit=MagicMock(), 
                                                       habit_completed=MagicMock()))
  
    
    def test_main_add_habit_and_exit(self, mock_program_menu, mock_select):
        """Test main function where user adds a habit and exits."""
        mock_select.side_effect = [
            MagicMock(ask=lambda: "Add, Delete, or Mark a Habit as complete"), 
            MagicMock(ask=lambda: "Add Habit"),  
            MagicMock(ask=lambda: "Exit Habit Hero")  
        ]
        main.main()

        user = mock_program_menu.return_value
        user.add_habit.assert_called_once()
        user.store_habit_in_db.assert_called_with("New Habit")

if __name__ == '__main__':
    unittest.main()
