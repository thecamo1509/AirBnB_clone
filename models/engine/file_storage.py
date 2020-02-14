import json


class FileStorage():
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[self.__class__.__name__] = obj

    def save(self):
        myjson = json.dumps(self.__objects)
        with open(self.__file_path, "w") as f:
            f.write(myjson)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                file = f.read()
                return file
        except FileNotFoundError:
            return
