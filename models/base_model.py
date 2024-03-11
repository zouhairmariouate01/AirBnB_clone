#!/usr/bin/env python3

"""
    base_model module.

    Module that contains, BaseModel class which all classes of inherit from.
"""


import uuid
import models
from datetime import datetime


class BaseModel:
    """
        BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
            BaseModel's Constructor.

            args (list): list of arguments, not not used.
            kwargs (dict): dictionary of attribute names and its values.
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            function that returns a string representation of
            the current object.

            Return:
                (str): string representation of the current object.
        """
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
            function that updates the current object, and assign the
            update_at with the current date & time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            function that returns a dictionary containing all keys/values
            of the instance.

            Return:
                (dict): dictionary containing all keys/values of
                current instance.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
