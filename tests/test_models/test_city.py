#!/usr/bin/python3
"""
Test for City class
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up an instance of City for testing."""
        self.city = City()

    def test_city_state_id_is_string(self):
        """Test if the state_id attribute of City is a string."""
        self.assertIsInstance(self.city.state_id, str)

    def test_city_name_is_string(self):
        """Test if the name attribute of City is a string."""
        self.assertIsInstance(self.city.name, str)

    def test_city_str_representation(self):
        """Test the string representation of City for the expected format."""
        str_representation = str(self.city)
        self.assertTrue(isinstance(str_representation, str))
        self.assertIn("[City]", str_representation)
        self.assertIn('id', str_representation)
        self.assertIn('state_id', str_representation)
        self.assertIn('name', str_representation)

    def test_city_to_dict(self):
        """Test if the to_dict method of City returns the expected dictionary."""
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    # Add more test functions based on your specific implementation of the City class

if __name__ == '__main__':
    unittest.main()
