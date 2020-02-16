#!/usr/bin/python3

import uuid
import models
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
            models.storage.new(self)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        models.storage.save()

    def to_dict(self):
        new_dir = self.__dict__.copy()
        new_dir["__class__"] = self.__class__.__name__
        new_dir["created_at"] = self.created_at.isoformat()
        new_dir["updated_at"] = self.updated_at.isoformat()
        return(new_dir)

    def delete(self):
        models.storage.delete(self)
