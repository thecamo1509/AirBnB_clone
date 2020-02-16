#!/usr/bin/python3

from models.base_model import BaseModel
"""
Public class that inherit from BaseModel
"""


class Review(BaseModel):
    """ Class Review
        Attributes:
        -----------
        place_id: string it will be the Place.id
        user_id: string it will be the User.id
        text: string
    """
    place_id = ""
    user_id = ""
    text = ""
