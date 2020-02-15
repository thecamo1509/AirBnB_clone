import json
import os.path as path
from ..base_model import BaseModel


class FileStorage():
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        c_n = obj.__class__.__name__ + "." + obj.id
        self.__objects[c_n] = obj

    def save(self):
        new_object = {}
        for key, value in self.__objects.items():
            new_object.update({key: value.to_dict()})
        myjson = json.dumps(new_object)
        with open(self.__file_path, "w") as f:
            f.write(myjson)

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_loads = json.load(f)
                for key, value in json_loads.items():
                    obj = BaseModel(**value)
                    self.__objects.update({key: obj})
                    print(self.__objects[key], ".............AHHHHHH!!!!")
