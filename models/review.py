#!/usr/bin/python3
"""Review class Module"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new Review instance
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def to_dict(self):
        """
        Returns a dictionary representation of the Review instance
        """
        base_dict = super().to_dict()
        review_dict = {
            "place_id": self.place_id,
            "user_id": self.user_id,
            "text": self.text
        }
        base_dict.update(review_dict)
        return base_dict

    def __str__(self):
        """
        Returns the string representation of the Review instance
        """
        return "[Review] ({}) {}".format(self.id, self.to_dict())