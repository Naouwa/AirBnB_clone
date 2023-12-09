#!/usr/bin/python3
"""Defining the FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    initializing the FileStorage class
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects
    by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
    }

    def all(self):
        """It returns the dictionary __objects __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """It sets in __objects the obj with key <obj_class_name>.id"""
        obj_cls = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls, obj.id)] = obj

    def save(self):
        """It serializes __objects to the JSON File"""
        object_dict = self.__objects
        new_data = {o: object_dict[o].to_dict() for o in object_dict.keys()}
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_data, f)

    def reload(self):
        """
        It deserialzes the JSON file to __objects
        (only if the JSON file exists)
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                object_dict = json.load(f)
                for obj in object_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
