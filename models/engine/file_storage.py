#!/usr/bin/python3
"""
File Storage Module
"""
import json
import os.path
class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects
    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized_dict, file)
    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_dict = json.load(file)
                for key, value in serialized_dict.items():
                    class_name, instance_id = key.split('.')
                    # Create an instance based on the class name
                    obj_cls = globals()[class_name]
                    instance = obj_cls(**value)
                    # Store the instance in __objects
                    self.__objects[key] = instance
        else:
            return
