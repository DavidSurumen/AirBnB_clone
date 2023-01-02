#!/usr/bin/python3
"""This module defines the class BaseModel."""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Defines all common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """constructor of a BaseModel."""
        if kwargs != {}:
            for key, val in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at' or \
                        key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(val)
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a human readable string repr of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute 'updated_at' with the current
        datetime."""
        self.updated_at = datetime.now()
        storage.new(self)   # to add the attribute 'update_now', and any other
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__ of the
        instance."""
        dict_ = self.__dict__.copy()
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        dict_['__class__'] = type(self).__name__
        return dict_
