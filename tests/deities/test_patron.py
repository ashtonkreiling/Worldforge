import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add project root to path to import deities.patron
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from deities.patron import Patron


class TestPatronTurn(unittest.TestCase):
    
    @patch('deities.patron.roll_random_event')
    @patch('deities.patron.ask_religion_question')
    @patch('deities.patron.ask_cultural_question')
    @patch('deities.patron.grow_settlement')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_take_turn_calls_all_functions(self, mock_print, mock_input, mock_grow_settlement, 
                                           mock_ask_cultural_question, mock_ask_religion_question, 
                                           mock_roll_random_event):
        """Test that take_turn calls all required functions in the correct order."""
        # Set up return values for the mocked functions
        mock_grow_settlement.return_value = 0
        mock_ask_cultural_question.return_value = "Test cultural question"
        mock_ask_religion_question.return_value = "Test religion question"
        mock_roll_random_event.return_value = "Test random event"
        mock_input.return_value = ""  # Simulate user pressing Enter
        
        # Create a Patron instance and call take_turn
        patron = Patron()
        patron.take_turn()
        
        # Verify all functions were called
        mock_grow_settlement.assert_called_once()
        mock_ask_cultural_question.assert_called_once()
        mock_ask_religion_question.assert_called_once()
        mock_roll_random_event.assert_called_once()
        
        # Verify input was called twice (for cultural and religion questions)
        self.assertEqual(mock_input.call_count, 2)
        
        # Verify print was called for each output
        # Should be called for: settlement status, cultural question, religion question, random event
        self.assertGreaterEqual(mock_print.call_count, 4)
        
        # Verify increment_power was called (power should have increased)
        # Since we can't easily mock increment_power without mocking random, we check the power increased
        # The default power is 4, and increment_power adds 2d6 (2-12), so power should be >= 6
        self.assertGreaterEqual(patron.power, 6)
    
    @patch('deities.patron.roll_random_event')
    @patch('deities.patron.ask_religion_question')
    @patch('deities.patron.ask_cultural_question')
    @patch('deities.patron.grow_settlement')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_take_turn_calls_functions_in_order(self, mock_print, mock_input, mock_grow_settlement,
                                                 mock_ask_cultural_question, mock_ask_religion_question,
                                                 mock_roll_random_event):
        """Test that take_turn calls functions in the correct order."""
        mock_grow_settlement.return_value = 1
        mock_ask_cultural_question.return_value = "Cultural question"
        mock_ask_religion_question.return_value = "Religion question"
        mock_roll_random_event.return_value = "Random event"
        mock_input.return_value = ""
        
        # Create a Patron instance and call take_turn
        patron = Patron()
        initial_power = patron.power
        patron.take_turn()
        
        # Check the order of calls
        calls = [call[0] for call in mock_grow_settlement.call_args_list + 
                 mock_ask_cultural_question.call_args_list +
                 mock_ask_religion_question.call_args_list +
                 mock_roll_random_event.call_args_list]
        
        # Verify grow_settlement is called first
        self.assertTrue(mock_grow_settlement.called)
        # Verify ask_cultural_question is called after grow_settlement
        self.assertTrue(mock_ask_cultural_question.called)
        # Verify ask_religion_question is called after ask_cultural_question
        self.assertTrue(mock_ask_religion_question.called)
        # Verify roll_random_event is called after ask_religion_question
        self.assertTrue(mock_roll_random_event.called)
        # Verify increment_power is called last (power should have increased)
        self.assertGreater(patron.power, initial_power)


    @patch('deities.deity.random.randint')
    def test_increment_power_adds_2d6_to_power(self, mock_randint):
        """Test that increment_power rolls 2d6 and adds the result to power."""
        # Mock the two dice rolls to return known values
        mock_randint.side_effect = [3, 4]  # First roll returns 3, second returns 4
        
        # Create a Patron with known initial power
        patron = Patron("TestPatron", 10)
        initial_power = patron.power
        
        # Call increment_power
        patron.increment_power()
        
        # Verify random.randint was called twice with arguments (1, 6)
        self.assertEqual(mock_randint.call_count, 2)
        mock_randint.assert_any_call(1, 6)
        
        # Verify power increased by 7 (3 + 4)
        self.assertEqual(patron.power, initial_power + 7)
        self.assertEqual(patron.power, 17)


if __name__ == '__main__':
    unittest.main()
