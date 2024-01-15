#!/usr/bin/python3

"""Defines the BaseModel class"""
import uuid
import models
from datetime import datetime

class BaseModel:
    """Base class for all models"""
    def __init__(self, *args, **kwargs):
        """Constructor for initializing the instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
    def __str__(self):
        """String representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Converts the instance to a dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict

    def save(self):
        """Saves the instance to the storage"""
        self.updated_at = datetime.now()
        models.storage.save()