#!/usr/bin/python3
"""This module defines the class BaseModel."""
import uuid
from datetime import datetime


class BaseModel():
    """Defines all common attributes and methods for other classes."""

    def __init__(self):
        """constructor."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def __str__(self):
        """Specifies value to be printed by __str__()"""
        return '[{}] ({}) {}'\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute 'updated_at' with the current
        datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__ of the
        instance."""
        dict_ = self.__dict__.copy()
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['__class__'] = self.__class__.__name__
        return dict_
