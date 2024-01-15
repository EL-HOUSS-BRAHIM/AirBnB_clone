#!/usr/bin/python3
"""Place class Module"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Place class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new Place instance
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    def to_dict(self):
        """
        Returns a dictionary representation of the Place instance
        """
        base_dict = super().to_dict()
        place_dict = {
            "city_id": self.city_id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "number_rooms": self.number_rooms,
            "number_bathrooms": self.number_bathrooms,
            "max_guest": self.max_guest,
            "price_by_night": self.price_by_night,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "amenity_ids": self.amenity_ids
        }
        base_dict.update(place_dict)
        return base_dict

    def __str__(self):
        """
        Returns the string representation of the Place instance
        """
        return "[Place] ({}) {}".format(self.id, self.to_dict())