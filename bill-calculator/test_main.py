from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io
import logging

from gradescope_utils.autograder_utils.decorators import weight

class Test(TestCase):
    @weight(0.5)
    def test_invalid_bill_type(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout, patch('builtins.input') as mock_input:
            for invalid_input in ['3', '-1', 'a', 'jklj123lj', '']:
                mock_input.return_value = invalid_input
                try:
                    import main
                except SystemExit:
                    pass
                try:
                    sys.modules.pop('main')
                except KeyError:
                    pass
                self.assertTrue('error' in mock_stdout.getvalue().lower())
                

    @patch('builtins.input', side_effect=["1", "76"])
    @weight(0.5)
    def test_elec_bill_low_rate(self, mock_input):
        expected_bill = 380
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            sys.modules.pop('main')
        self.assertTrue(str(expected_bill) in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["1", "440"])
    @weight(0.5)
    def test_elec_bill_med_rate(self, mock_input):
        expected_bill = 4400
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            sys.modules.pop('main')
        self.assertTrue(str(expected_bill) in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["1", "1500"])
    @weight(0.5)
    def test_elec_bill_high_rate(self, mock_input):
        expected_bill = 22500
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            sys.modules.pop('main')
        self.assertTrue(str(expected_bill) in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["2", "401"])
    @weight(0.5)
    def test_water_bill_low_rate(self, mock_input):
        expected_bill = 20050
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            sys.modules.pop('main')
        self.assertTrue(str(expected_bill) in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["2", "1900"])
    @weight(0.5)
    def test_water_bill_med_rate(self, mock_input):
        expected_bill = 114000
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            sys.modules.pop('main')
        self.assertTrue(str(expected_bill) in mock_stdout.getvalue())

    @patch('builtins.input', side_effect=["2", "3500"])
    @weight(0.5)
    def test_water_bill_high_rate(self, mock_input):
        expected_bill = 245000
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            sys.modules.pop('main')
        self.assertTrue(str(expected_bill) in mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
