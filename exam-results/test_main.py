from unittest.mock import patch
from unittest import TestCase
import unittest
import sys

class Test(TestCase):
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["99"])
    def test_high_score(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("You passed!")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["65"])
    def test_fail(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("Try again")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["70"])
    def test_70(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("Try again")
        finally:
            sys.modules.pop('main')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["71"])
    def test_71(self, mock_input, mock_print):
        import main
        try:
            mock_print.assert_called_with("You passed!")
        finally:
            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
