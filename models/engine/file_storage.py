import json
import os.path as path
from ..base_model import BaseModel


class FileStorage():
    """
    FileStorage class: that serializes and deserializes
    a JSON file to instances
    Attributes:
    ----------
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Public method that returns the dictionary __objects
        """
        return(self.__objects)

    def new(self, obj):
        """
        Public method that sets in __objects the obj with key
        """
        c_n = obj.__class__.__name__ + "." + obj.id
        self.__objects[c_n] = obj

    def save(self):
        """
        Public method that serializes __objects to the JSON file
        """
        new_object = {}
        for key, value in self.__objects.items():
            new_object.update({key: value.to_dict()})
        myjson = json.dumps(new_object)
        with open(self.__file_path, "w") as f:
            f.write(myjson)

    def delete(self, obj=None):
        """
        Public method that deletes an instance based on the class
        """
        if obj is not None:
            del self.__objects[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def reload(self):
        """
        Public method that deserializes the JSON file to __objects
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_loads = json.load(f)
                for key, value in json_loads.items():
                    obj = BaseModel(**value)
                    self.__objects.update({key: obj})
