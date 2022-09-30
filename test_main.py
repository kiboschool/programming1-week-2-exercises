from unittest.mock import patch
from unittest import TestCase
import unittest
import sys

class Test(TestCase):
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1", "21"])
    def test_enough_for_one(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("You have enough money, go for it!")
        sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["3", "61"])
    def test_enough_for_three(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("You have enough money, go for it!")
        sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1", "19"])
    def test_short_for_one(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("You need $1 more to buy that number of books")
        sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["3", "15"])
    def test_short_for_three(self, mock_input, mock_print):
        import main
        mock_print.assert_called_with("You need $45 more to buy that number of books")

if __name__ == '__main__':
    unittest.main()
