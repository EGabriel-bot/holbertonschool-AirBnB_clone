#!/usr/bin/env python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent a storage engine.
    
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        new = {}
        with open(self.__file_path, 'w', encoding="utf-8") as json_file:
            for key, value in self.__objects.items():
                new.update({key: value.to_dict()})
            json_file.write(json.dumps(new))

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for o in json.load(file).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
