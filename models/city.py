#!/usr/bin/python3

from models.base_model import BaseModel
"""
Public class that inherit from BaseModel
"""


class City(BaseModel):
    """ Class City
        Attributes:
        -----------
        state_id: string: it will be the State.id
        name: string City name
    """
    state_id = ""
    name = ""
