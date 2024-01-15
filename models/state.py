#!/usr/bin/python3
"""State class Module"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new State instance
        """
        super().__init__(*args, **kwargs)
        self.name = ""

    def to_dict(self):
        """
        Returns a dictionary representation of the State instance
        """
        base_dict = super().to_dict()
        state_dict = {
            "name": self.name
        }
        base_dict.update(state_dict)
        return base_dict

    def __str__(self):
        """
        Returns the string representation of the State instance
        """
        return "[State] ({}) {}".format(self.id, self.to_dict())
