#!/usr/bin/python3
"""
Test for Place class
"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up an instance of Place for testing."""
        self.place = Place()

    def test_place_city_id_is_string(self):
        """Test if the city_id attribute of Place is a string."""
        self.assertIsInstance(self.place.city_id, str)

    def test_place_user_id_is_string(self):
        """Test if the user_id attribute of Place is a string."""
        self.assertIsInstance(self.place.user_id, str)

    def test_place_name_is_string(self):
        """Test if the name attribute of Place is a string."""
        self.assertIsInstance(self.place.name, str)

    def test_place_description_is_string(self):
        """Test if the description attribute of Place is a string."""
        self.assertIsInstance(self.place.description, str)

    def test_place_number_rooms_is_int(self):
        """Test if the number_rooms attribute of Place is an integer."""
        self.assertIsInstance(self.place.number_rooms, int)

    # Add more test functions based on your specific implementation of the Place class

    def test_place_str_representation(self):
        """Test the string representation of Place for the expected format."""
        str_representation = str(self.place)
        self.assertTrue(isinstance(str_representation, str))
        self.assertIn("[Place]", str_representation)
        self.assertIn('id', str_representation)
        self.assertIn('city_id', str_representation)
        self.assertIn('user_id', str_representation)
        self.assertIn('name', str_representation)
        self.assertIn('description', str_representation)

    def test_place_to_dict(self):
        """Test if the to_dict method of Place returns the expected dictionary."""
        place_dict = self.place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')

if __name__ == '__main__':
    unittest.main()
