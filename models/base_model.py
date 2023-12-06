#!/usr/bin/python3
"""The Basemodel class Module"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class and all its common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Initialzing the BaseModel and its public instances"""
        date_fromat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Implements the string method"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """It saves the updated date & time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """The representation of dict"""
        dic_repr = self.__dict__.copy()
        dic_repr["__class__"] = self.__class__.__name__
        dic_repr["created_at"] = self.created_at.isoformat()
        dic_repr["updated_at"] = self.updated_at.isoformat()
        return dic_repr
