#!/usr/bin/env python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

"""
    Module of FileStorage.
"""


class FileStorage:
    """
        class FileStorage.

        This class has methods that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Method that returns all objects stored.
            Return:
                objects (dict): dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj=None):
        """
            Method that sets new objects to the dictionary.
        """
        if obj is None:
            return
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
            Method that serialize all objects to a JSON file.
        """
        if FileStorage.__file_path == "" or FileStorage.__file_path is None:
            return
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, file)

    def classes(self, name):
        """
            Method that returns a specific class from its name.
            Return:
                class (class): return class from its name.
        """
        d = {
            "BaseModel": BaseModel, "User": User, "City": City,
            "Amenity": Amenity, "State": State, "Review": Review,
            "Place": Place
        }
        if name in d:
            return d[name]
        else:
            return None

    def reload(self):
        """
            Method that deserialize JSON file to a dictionary of objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r',
                      encoding='UTF-8') as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
