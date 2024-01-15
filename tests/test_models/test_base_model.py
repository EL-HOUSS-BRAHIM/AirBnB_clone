#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """Set up an instance of BaseModel for testing."""
        self.base_model = BaseModel()

    def test_base_model_id_is_string(self):
        """Test if the id attribute of BaseModel is a string."""
        self.assertIsInstance(self.base_model.id, str)

    def test_base_model_created_at_is_datetime(self):
        """Test if the created_at attribute of BaseModel is a datetime object."""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_base_model_updated_at_is_datetime(self):
        """Test if the updated_at attribute of BaseModel is a datetime object."""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_base_model_str_representation(self):
        """Test the string representation of BaseModel for the expected format."""
        str_representation = str(self.base_model)
        self.assertTrue(isinstance(str_representation, str))
        self.assertIn("[BaseModel]", str_representation)
        self.assertIn('id', str_representation)

    def test_base_model_to_dict(self):
        """Test if the to_dict method of BaseModel returns the expected dictionary."""
        base_model_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertIn('__class__', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_base_model_save_updates_updated_at(self):
        """Test if the save method of BaseModel updates the updated_at attribute."""
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

if __name__ == '__main__':
    unittest.main()
