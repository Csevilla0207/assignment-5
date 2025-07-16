"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

from unittest import TestCase
from unittest.mock import patch
from src.chatbot import get_account_number

__author__ = "Kimi Sevilla"
__version__ = ""
__credits__ = "COMP-1327 Faculty"

class TestChatBot(TestCase):

    def test_type_error_when_input_not_init(self):
        user_input = "non_numeric_data"
        with patch('builtins.input', return_value=user_input):
            with self.assertRaises(TypeError) as cm:
                get_account_number

            self.assertEqual(str(cm.exception), "Account number must be an int type. ")

        

    def test_value_error_when_account_not_exist(self):
        user_input = "112233"
        with patch('builtins.input', return_value=user_input):
            # Act & Assert
            with self.assertRaises(ValueError) as cm:
                get_account_number()

            self.assertEqual(str(cm.exception), "Account number entered does not exist.")
        

    def test_valid_account_number_returned(self):
          user_input = "123456"
          with patch('builtins.input', return_value=user_input):
              result = get_account_number()
              self.assertEqual(result, 123456)






    
