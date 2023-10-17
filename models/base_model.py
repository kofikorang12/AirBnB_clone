#!/usr/bin/python3
"""
    base_model module
    The module defines the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class defines all common attributes for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
       The constructor for the BaseModel class that init the public instances
            a) id
            b) created_at
            c) updated_at
        Updating the constructor arguments to account for *args
            and kwargs. kwargs if present would be used to create a new
            instance of the BaseModel instead.
        """
        if kwargs and len(kwargs) > 0:
            fmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    kwargs[key] = datetime.strptime(val, fmt)
                self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """overriding the toString method"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ current BaseModel instance
        """
        my_dict = {}
        for key, val in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = val.isoformat()
            elif key == "number":
                my_dict["my_number"] = val
            else:
                my_dict[key] = val
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
