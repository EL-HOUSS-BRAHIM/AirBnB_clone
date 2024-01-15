#!/usr/bin/python3
"""City class Module"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the City class
        """
        super().__init__(*args, **kwargs)
        # Add specific attributes for the City class
        self.state_id = ""
        self.name = ""

# If this module is run independently, the following block will execute
if __name__ == "__main__":
    # Create an instance of City and print its representation
    city_instance = City()
    print(city_instance)
