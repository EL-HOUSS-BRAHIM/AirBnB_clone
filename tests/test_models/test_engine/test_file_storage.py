#!/usr/bin/python3
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
import os

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up a clean instance of FileStorage for each test."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up resources after each test."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """Test that FileStorage initializes correctly."""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method(self):
        """Test the all() method of FileStorage."""
        # Ensure the initial state is an empty dictionary
        self.assertEqual(self.storage.all(), {})

        # Add some objects and check if they are in the dictionary
        obj1 = BaseModel()
        obj2 = Amenity()
        self.storage.new(obj1)
        self.storage.new(obj2)
        expected_dict = {
            "BaseModel." + obj1.id: obj1,
            "Amenity." + obj2.id: obj2
        }
        self.assertEqual(self.storage.all(), expected_dict)

    def test_new_method(self):
        """Test the new() method of FileStorage."""
        obj1 = BaseModel()
        obj2 = Amenity()

        # Add objects using the new() method
        self.storage.new(obj1)
        self.storage.new(obj2)
        expected_dict = {
            "BaseModel." + obj1.id: obj1,
            "Amenity." + obj2.id: obj2
        }
        self.assertEqual(self.storage.all(), expected_dict)

    def test_save_method(self):
        """Test the save() method of FileStorage."""
        obj1 = BaseModel()
        obj2 = Amenity()
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Save the objects to file
        self.storage.save()

        # Read the contents of the file and check if it matches the expected dictionary
        with open(FileStorage._FileStorage__file_path, 'r', encoding="utf-8") as file:
            saved_dict = json.load(file)

        expected_dict = {
            "BaseModel." + obj1.id: obj1.to_dict(),
            "Amenity." + obj2.id: obj2.to_dict()
        }
        self.assertEqual(saved_dict, expected_dict)

    def test_reload_method(self):
        """Test the reload() method of FileStorage."""
        obj1 = BaseModel()
        obj2 = Amenity()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Clear the objects in memory and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        expected_dict = {
            "BaseModel." + obj1.id: obj1,
            "Amenity." + obj2.id: obj2
        }
        self.assertEqual(self.storage.all(), expected_dict)

if __name__ == "__main__":
    unittest.main()
