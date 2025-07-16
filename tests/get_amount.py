from unittest import TestCase
from unittest.mock import patch
from src.chatbot import get_account_number, get_amount

class TestChatbot(TestCase):

    def test_type_error_when_input_not_int(self):


class TestGetAmount(TestCase):

    def test_type_error_when_amount_not_numeric(self):
        # Arrange
        user_input = "abc"

        with patch('builtins.input', return_value=user_input):
            # Act & Assert
            with self.assertRaises(TypeError) as cm:
                get_amount()

            # Assert
            self.assertEqual(str(cm.exception), "Amount must be a numeric type.")

    def test_value_error_when_amount_zero(self):
        # Arrange
        user_input = "0"

        with patch('builtins.input', return_value=user_input):
            # Act & Assert
            with self.assertRaises(ValueError) as cm:
                get_amount()

            # Assert
            self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    def test_value_error_when_amount_negative(self):
        # Arrange
        user_input = "-5.50"

        with patch('builtins.input', return_value=user_input):
            # Act & Assert
            with self.assertRaises(ValueError) as cm:
                get_amount()

            # Assert
            self.assertEqual(str(cm.exception), "Amount must be a value greater than zero.")

    def test_valid_amount_returned(self):
        # Arrange
        user_input = "123.45"

        with patch('builtins.input', return_value=user_input):
            # Act
            result = get_amount()

            # Assert
            self.assertEqual(result, 123.45)
