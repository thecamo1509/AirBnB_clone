#!/usr/bin/python3

import uuid
import models
from datetime import datetime


class BaseModel():
    """ Class BaseModel: that defines all common attributes/methods
        for other classes
    """
    def __init__(self, *args, **kwargs):
        """ Constructor class
        Attributes
        ----------
        *args: list argument (won’t be used)
        **kwargs: dictionary of arguments
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if (key != '__class__'):
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Method to return a string
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        Method updates the public instance attribute updated_at
        with the current datetime
        """
        models.storage.save()

    def to_dict(self):
        """
        Method to returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        new_dir = self.__dict__.copy()
        new_dir["__class__"] = self.__class__.__name__
        new_dir["created_at"] = self.created_at.isoformat()
        new_dir["updated_at"] = self.updated_at.isoformat()
        return(new_dir)

    def delete(self):
        """
        Method to deletes an instance based on the class name
        """
        models.storage.delete(self)
