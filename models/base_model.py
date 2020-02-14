#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel():
    def __init__(self, *args, **kwargs):

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

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dir = self.__dict__.copy()
        new_dir["__class__"] = self.__class__.__name__
        new_dir["created_at"] = new_dir["created_at"].isoformat()
        new_dir["updated_at"] = new_dir["updated_at"].isoformat()
        return (new_dir)
