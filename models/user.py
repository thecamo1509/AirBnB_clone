#!/usr/bin/python3

from models.base_model import BaseModel
"""
Public class that inherit from BaseModel
"""


class User(BaseModel):
    """ Class State
        Attributes:
        -----------
        email: string
        password: string
        first_name: string
        last_name: string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
