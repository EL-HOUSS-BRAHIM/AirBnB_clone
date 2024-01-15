#!/usr/bin/python3
"""Amenity class Module"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class for storing information about amenities."""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

    def to_dict(self):
        """Convert Amenity instance to a dictionary."""
        amenity_dict = super().to_dict()
        amenity_dict["name"] = self.name
        return amenity_dict

    def __str__(self):
        """Return a string representation of Amenity instance."""
        return "[Amenity] ({}) {}".format(self.id, self.to_dict())