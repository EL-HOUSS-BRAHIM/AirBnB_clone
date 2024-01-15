#!/usr/bin/python3
"""
Test for State class
"""

import unittest
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up an instance of State for testing."""
        self.state = State()

    def test_state_name_is_string(self):
        """Test if the name attribute of State is a string."""
        self.assertIsInstance(self.state.name, str)

    # Add more test functions based on your specific implementation of the State class

    def test_state_str_representation(self):
        """Test the string representation of State for the expected format."""
        str_representation = str(self.state)
        self.assertTrue(isinstance(str_representation, str))
        self.assertIn("[State]", str_representation)
        self.assertIn('id', str_representation)
        self.assertIn('name', str_representation)

    def test_state_to_dict(self):
        """Test if the to_dict method of State returns the expected dictionary."""
        state_dict = self.state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')

if __name__ == '__main__':
    unittest.main()
