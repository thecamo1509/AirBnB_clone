import json
import os.path as path


class FileStorage():
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        ids = obj["id"]
        name = obj["__class__"]
        complete_name = name + "." + ids
        self.__objects[complete_name] = obj
        
    def save(self):
        myjson = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(myjson)

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                files= f.read()
                self.__objects = json.loads(files)
