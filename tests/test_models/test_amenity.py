#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):

    def setUp(self):
        """Set up an instance of Amenity for testing."""
        self.amenity = Amenity()

    def test_amenity_inherits_from_base_model(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test the presence and types of attributes in Amenity."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_to_dict(self):
        """Test if the to_dict method of Amenity returns the expected dictionary."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_amenity_str_representation(self):
        """Test the string representation of Amenity for the expected format."""
        str_repr = str(self.amenity)
        self.assertIn("[Amenity]", str_repr)
        self.assertIn("'id':", str_repr)
        self.assertIn("'created_at':", str_repr)
        self.assertIn("'updated_at':", str_repr)

if __name__ == '__main__':
    unittest.main()