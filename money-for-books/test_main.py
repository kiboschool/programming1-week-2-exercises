from unittest.mock import patch
from unittest import TestCase
import unittest
import sys

from gradescope_utils.autograder_utils.decorators import weight

class Test(TestCase):
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1", "21"])
    @weight(0.5)
    def test_enough_for_one(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("You have enough money, go for it!")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["3", "61"])
    @weight(0.5)
    def test_enough_for_three(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("You have enough money, go for it!")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1", "19"])
    @weight(0.5)
    def test_short_for_one(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("You need $1 more to buy that number of books")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["3", "15"])
    @weight(0.5)
    def test_short_for_three(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("You need $45 more to buy that number of books")
        finally:
            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
